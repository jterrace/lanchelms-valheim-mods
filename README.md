# LanChelms Valheim Mods

A pack of mods for the LanChelms Deep North Valheim server.

We are starting a server that will run ~1 month per boss after Eikthyr. To keep a
server running for 7+ months, we've created this mod pack for all players and the
server to keep in sync.

The core philosophy here is to enhance the game in a way that increases everyone's
fun without altering the game too radically. We want to maximize our enjoyment of the
game without modifying it too far from its intended design.

## Core/Server

[BepInEx] is required for modding so that's a given. [Server_devcommands] is required for admins to have dev commands, but note that we
are not using dev commands regularly: it's only added for any rare occasions we might need it. [ServerCharacters] stores your character
file on the server and enforces that each Steam user can only have a single character. [Where_You_At] forces players to be visible
on the map since people often forget to turn it on and we're not doing PvP here. [MaxPlayerCount] is required to increase the max player
count above 10, and [DiscordConnector] posts information to our Discord about the server. [BetterNetworking_Valheim] improves networking
performance with a large player count and prevents network data loss. [BetterSleepBruh] improves the sleep behavior for a multiplayer server
where it's often impossible to coordinate everyone to sleep. [TimeoutLimit] increases the connection timeout from 30 seconds to 90 seconds,
which helps with Steam Deck slow connection times. [VentureMultiplayerTweaks] is brought in so we can have PVP battles without skill loss
or teleportation back to your bed.

## Enforcements

We don't want to burden players with lengthy rules that admins have to enforce. Instead, our approach is to let mods enforce the rules.
First, [AzuAntiCheat] requires that everyone has the same mods. [BiomeLock] and [World_Advancement_Progression] work together. First,
BiomeLock makes it so a debuff indicator appears when you enter a biome we haven't unlocked yet. It also makes it so you can't pick up
loot, mine ore, use the hammer, or interact with pickables. This keeps players from progressing into locked biomes. If somehow you do
manage to acquire items from a later biome, World Advancement Progression prevents crafting of items you shouldn't be making yet.

## Resources

We configure the resource rate to 3x. This lets us spend less time farming and more time having fun. Some resource
locations can end up being diminished on a large multiplayer server. To address that, we add [StumpsRegrow] to allow trees to regrow
instead of winding up with a barren wasteland of a starting island. [Venture_Location_Reset] is configured to respawn many of the points
of interest like Fuling camps, Burial Chambers, Sunken Crypts, etc. This ensures everyone has a chance to acquire materials from these
areas. [Mining_Caves] adds a couple additional caves that will reset to acquire materials like Copper, Tin, and Silver, which normally
have no way of resetting. Finally, we add [TradersExtended] and configure it to have some additional items like the early axes, which
normally can't be acquired by everyone. We make these rare items purchasable with gold so everyone has a chance to use them.

## Inventory

The Valheim developers have made it very clear that they consider inventory management to be a core part of the game, even if players
hate the toil associated with it. We address this with mods.

[AzuCraftyBoxes] allows you to craft using items from nearby containers because pulling items manually is incredibly tedious.
[AzuExtendedPlayerInventory] adds dedicated equipment slots instead of having to use inventory slots for equipment, which is one
of the most requested features that devs refuse to add. We also configure an extra row of inventory to start and will add more as we
progress later in the game. Otherwise, you end up with only a few slots of space in the Ashlands which is miserable. [ItemStacksItemWeights]
lets us configure the stack size of items to be 3x their base. This pairs nicely with 3x resource rate so items don't pile up in chests.

Since we have 3x resource and stack size, carry weight needs to be increased as well. Rather than a fixed multiplier, we add
[SkilledCarryWeight], which is a fun way to increase the weight you can carry based on your skills. This makes it increase over time and
gives players a reason to level skills. Finally, [AzuAnti-ArthriticCrafting] is added to make crafting less time consuming: adding a search
bar to find items, allows you to specify the number of items to craft, and lets you track recipes.

## Cosmetic

We've added a collection of mods that are mostly cosmetic to enhance the world. [ShipwrightsTouch] and [LongShip Upgrades] add fun
new sail colors and textures players can configure to make their boats unique. It also allows upgrading the longship for some extra
storage and health. [Seasonality] is configured to change the world's textures for each season, which makes the world feel more
dynamic. The seasons are cosmetic only, with all of the world property changes turned off.

We've also added a few mods to address some of the largest complaints about the Mistlands biome. [Better_Wisps] allows upgrading the
wisp for a larger radius, and [Mistward] adds a new building that wards off mist in a large radius. [Foglands] changes
the mist to be more subtle instead of the default mist that completely blocks out the world, causes motion sickness for some people,
and is generally oppressive. Combined, these make the Mistlands a much more enjoyable experience.

## Quality of Life

Broadly categorized as quality of life mods, these things make the game more fun and easier to play. [ServerSideMap] instantly
shares everyone's map discoveries and pins with everyone else. The map table is buggy, and requires that people remember to use it.
Being able to see what other people are discovering in real time is much more fun.

[ValheimInfiniteFire] keeps fires and light sources lit without having to fuel them. Spending time building light sources into your
large build just for it to go dark and require running around fueling it for several minutes is not our idea of fun. It's especially
annoying on multiplayer servers when other people might be close enough to drain your fuel when you're not even online.

[TargetPortal] is an absolute game changer. Large multiplayer servers end up littered with portals all over the place without clear
ownership, and it's chaos knowing how to get places. Instead of having to pair portals, TargetPortal shows all portals on the map
and lets you click on your destination.

[SpeedyPaths] increases your movement speed on dirt paths, wooden floors, and stone paths. This incentives people to build
roads, which is great for multiplayer villages and networks. [AzuWearNTearPatches] is brought in to remove water damage on boats,
to avoid the game's poor multiplayer ship physics.

[PlantEasily] allows for planting and harvesting crops in batches. Without it, farming quickly becomes a monotonous chore that
nobody enjoys.

## Creativity

We want people to build magnificent things. We bring in [Gizmo] to allow for multiple axes of rotation when building items. This
makes for some really amazing ways to build. [PlantEverything] allows planting all kinds of things, which makes for some outstanding
landscaping possibilities. We prefer people don't abuse it for farming. [AllTameableTamingOverhaul] is configured to bring in some
additional tameable creatures. This makes taming more fun, especially for biomes that don't have native tameables.

[BepInEx]: https://thunderstore.io/c/valheim/p/denikson/BepInExPack_Valheim/
[ServerCharacters]: https://thunderstore.io/c/valheim/p/Smoothbrain/ServerCharacters/
[Where_You_At]: https://thunderstore.io/c/valheim/p/Azumatt/Where_You_At/
[Server_devcommands]: https://thunderstore.io/c/valheim/p/JereKuusela/Server_devcommands/
[MaxPlayerCount]: https://thunderstore.io/c/valheim/p/Azumatt/MaxPlayerCount/
[DiscordConnector]: https://thunderstore.io/c/valheim/p/nwesterhausen/DiscordConnector/
[BetterNetworking_Valheim]: https://thunderstore.io/c/valheim/p/tibijczyk/BetterNetworking_Valheim/
[BetterSleepBruh]: https://thunderstore.io/c/valheim/p/Vapok/BetterSleepBruh/
[AzuAntiCheat]: https://thunderstore.io/c/valheim/p/Azumatt/AzuAntiCheat/
[BiomeLock]: https://thunderstore.io/c/valheim/p/Radamanto/BiomeLock/
[World_Advancement_Progression]: https://thunderstore.io/c/valheim/p/VentureValheim/World_Advancement_Progression/
[AzuCraftyBoxes]: https://thunderstore.io/c/valheim/p/Azumatt/AzuCraftyBoxes/
[AzuExtendedPlayerInventory]: https://thunderstore.io/c/valheim/p/Azumatt/AzuExtendedPlayerInventory/
[ItemStacksItemWeights]: https://thunderstore.io/c/valheim/p/shudnal/ItemStacksItemWeights/
[SkilledCarryWeight]: https://thunderstore.io/c/valheim/p/Searica/SkilledCarryWeight/
[AzuAnti-ArthriticCrafting]: https://thunderstore.io/c/valheim/p/Azumatt/AAA_Crafting/
[TradersExtended]: https://thunderstore.io/c/valheim/p/shudnal/TradersExtended/
[Venture_Location_Reset]: https://thunderstore.io/c/valheim/p/VentureValheim/Venture_Location_Reset/
[Mining_Caves]: https://thunderstore.io/c/valheim/p/VentureValheim/Mining_Caves/
[StumpsRegrow]: https://thunderstore.io/c/valheim/p/Advize/StumpsRegrow/
[ShipwrightsTouch]: https://thunderstore.io/c/valheim/p/malafein/ShipwrightsTouch/
[LongShip Upgrades]: https://thunderstore.io/c/valheim/p/shudnal/LongshipUpgrades/
[Foglands]: https://thunderstore.io/c/valheim/p/Azumatt/Foglands/
[Better_Wisps]: https://thunderstore.io/c/valheim/p/Digitalroot/Better_Wisps/
[Mistward]: https://thunderstore.io/c/valheim/p/MidnightMods/Mistward/
[Seasonality]: https://thunderstore.io/c/valheim/p/RustyMods/Seasonality/
[ServerSideMap]: https://thunderstore.io/c/valheim/p/Mydayyy/ServerSideMap/
[PlantEasily]: https://thunderstore.io/c/valheim/p/Advize/PlantEasily/
[ValheimInfiniteFire]: https://thunderstore.io/c/valheim/p/MidnightMods/ValheimInfiniteFire/
[SpeedyPaths]: https://thunderstore.io/c/valheim/p/Nextek/SpeedyPaths/
[TargetPortal]: https://thunderstore.io/c/valheim/p/Smoothbrain/TargetPortal/
[PlantEverything]: https://thunderstore.io/c/valheim/p/Advize/PlantEverything/
[AllTameableTamingOverhaul]: https://thunderstore.io/c/valheim/p/Meldurson/AllTameableTamingOverhaul/
[Gizmo]: https://thunderstore.io/c/valheim/p/ComfyMods/Gizmo/
[AzuWearNTearPatches]: https://thunderstore.io/c/valheim/p/Azumatt/AzuWearNTearPatches/
[TimeoutLimit]: https://thunderstore.io/c/valheim/p/MSchmoecker/TimeoutLimit/
[VentureMultiplayerTweaks]: https://thunderstore.io/c/valheim/p/VentureValheim/Venture_Multiplayer_Tweaks/
