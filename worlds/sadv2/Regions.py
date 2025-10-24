import typing

from BaseClasses import Region, MultiWorld, Location, Entrance
from .Locations import leaf_forest_locations, hot_crater_locations, music_plant_locations, ice_paradise_locations, \
                        sky_canyon_locations, techno_base_locations, egg_utopia_locations, xx_locations, SADV2Location, \
                        all_locations
from .Items import zone_table, SADV2Item
from .Options import SADV2Options

class SADV2Region(Region):
    game: str = "Sonic Advance 2"

def create_regions(world: MultiWorld, options: SADV2Options, player: int):
    menu_region = Region("Menu", player, world, "Zone Select")
    world.regions.append(menu_region)

    leaf_forest = create_region("Leaf Forest", player, world)
    create_locations(leaf_forest, "Sonic - Leaf Forest Act 1", "Sonic - Leaf Forest Act 2", 
                     "Sonic - Leaf Forest Boss Act")
    connect(world, player, "Menu", "Leaf Forest", 
            lambda state: (state.has("Leaf Forest", player)))

    hot_crater = create_region("Hot Crater", player, world)
    create_locations(hot_crater, "Sonic - Hot Crater Act 1", "Sonic - Hot Crater Act 2",
                     "Sonic - Hot Crater Boss Act")
    connect(world, player, "Menu", "Hot Crater",
            lambda state: (state.has("Hot Crater", player)))

    music_plant = create_region("Music Plant", player, world)
    create_locations(music_plant, "Sonic - Music Plant Act 1", "Sonic - Music Plant Act 2", 
                     "Sonic - Music Plant Boss Act")
    connect(world, player, "Menu", "Music Plant",
            lambda state: (state.has("Music Plant", player)))

    ice_paradise = create_region("Ice Paradise", player, world)
    create_locations(ice_paradise, "Sonic - Ice Paradise Act 1", "Sonic - Ice Paradise Act 2",
                     "Sonic - Ice Paradise Boss Act")
    connect(world, player, "Menu", "Ice Paradise",
            lambda state: (state.has("Ice Paradise", player)))

    sky_canyon = create_region("Sky Canyon", player, world)
    create_locations(sky_canyon, "Sonic - Sky Canyon Act 1", "Sonic - Sky Canyon Act 2",
                     "Sonic - Sky Canyon Boss Act")
    connect(world, player, "Menu", "Sky Canyon",
            lambda state: (state.has("Sky Canyon", player)))

    techno_base = create_region("Techno Base", player, world)
    create_locations(techno_base, "Sonic - Techno Base Act 1", "Sonic - Techno Base Act 2",
                     "Sonic - Techno Base Boss Act")
    connect(world, player, "Menu", "Techno Base",
            lambda state: (state.has("Techno Base", player)))

    egg_utopia = create_region("Egg Utopia", player, world)
    create_locations(egg_utopia, "Sonic - Egg Utopia Act 1", "Sonic - Egg Utopia Act 2", 
                     "Sonic - Egg Utopia Boss Act")
    connect(world, player, "Menu", "Egg Utopia",
            lambda state: (state.has("Egg Utopia", player)))

    xx = create_region("XX", player, world)
    create_locations(xx, "Sonic - XX")
    connect(world, player, "Menu", "XX",
            lambda state: (state.has("Red Chaos Emerald", player) and
                           state.has("Blue Chaos Emerald", player) and
                           state.has("Yellow Chaos Emerald", player) and
                           state.has("Green Chaos Emerald", player) and
                           state.has("White Chaos Emerald", player) and
                           state.has("Cyan Chaos Emerald", player) and
                           state.has("Purple Chaos Emerald", player)))
    
    xx.add_event("True Area 53", "Vanilla Rescued", location_type=SADV2Location, item_type=SADV2Item)



def create_region(name: str, player: int, world: MultiWorld) -> SADV2Region:
    region = SADV2Region(name, player, world)
    world.regions.append(region)

    return region

def create_locations(region: Region, *locations: str):
    region.locations += [SADV2Location(region.player, location_name, all_locations[location_name], region) for location_name in locations]

def connect(world: MultiWorld, player: int, outer_region: str, inner_region: str, \
            rule: typing.Optional[typing.Callable] = None):
    outer = world.get_region(outer_region, player)
    inner = world.get_region(inner_region, player)
    return outer.connect(inner, rule=rule)