import os
import shutil
import yaml
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

profile_dir_env = os.getenv("R2MODMAN_PROFILE_DIR")
assert profile_dir_env, "ERROR: R2MODMAN_PROFILE_DIR not found in .env file."
r2_profile_dir = Path(profile_dir_env)
r2_config_dir = r2_profile_dir / "BepInEx" / "config"
mods_yml_path = r2_profile_dir / "mods.yml"
assert r2_config_dir.exists(), f"ERROR: The directory {r2_config_dir} does not exist."
assert mods_yml_path.exists(), f"ERROR: Could not find {mods_yml_path}."
repo_config = Path("./config")
toml_path = Path("thunderstore.toml")

print(f"Syncing config files from: {r2_config_dir}")
shutil.rmtree(repo_config, ignore_errors=True)
shutil.copytree(
    r2_config_dir,
    repo_config,
    ignore=shutil.ignore_patterns(
        "*.bin",
        "*.log",
        "*.old",
        "*.txt",
        "binds.yaml",
        "permissions.yaml",
        "LastSeasonChangeData",
        # Contains webhook URL that should not be on client
        "Azumatt.AzuAntiCheat_Webhook.yml",
        # Configured server side due to encryption key
        "org.bepinex.plugins.servercharacters.cfg",
        # Contains webhook URL that should not be on client
        "games.nwest.valheim.discordconnector",
    ),
)

print(f"Reading active mod list from: {mods_yml_path}")
with open(mods_yml_path, "r", encoding="utf-8") as f:
    mods_data = yaml.safe_load(f)

dependencies = []
for mod in mods_data:
    if not mod.get("enabled"):
        continue
    # "Author-ModName"
    if not (name_part := mod.get("name")):
        continue
    # Grab the nested versionNumber dictionary
    if not (v := mod.get("versionNumber")):
        continue
    # Reconstruct the semantic version string
    version_part = f"{v.get('major', 0)}.{v.get('minor', 0)}.{v.get('patch', 0)}"
    # Thunderstore wants: "Author-ModName" = "1.2.3"
    dependencies.append(f'"{name_part}" = "{version_part}"')
dependencies = sorted(dependencies)

print(f"Found {len(dependencies)} active dependencies: {'\n  '.join(dependencies)}")

print("Updating thunderstore.toml dependencies...")
with open(toml_path, "r", encoding="utf-8") as f:
    toml_lines = f.readlines()

new_toml_lines = []
for line in toml_lines:
    new_toml_lines.append(line)
    # Copy everything exactly as is, until we hit the dependencies header
    if line.strip() == "[package.dependencies]":
        break

# Append our dynamically generated list of active mods
for dep in dependencies:
    new_toml_lines.append(f"{dep}\n")

with open(toml_path, "w", encoding="utf-8") as f:
    f.writelines(new_toml_lines)

print(f"Success! Synced configs and updated {len(dependencies)} dependencies.")
