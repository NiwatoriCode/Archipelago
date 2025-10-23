import typing

from BaseClasses import Region, Multiworld, Location, Entrance
from Locations import leaf_forest_locations, hot_crater_locations, music_plant_locations, ice_paradise_locations, \
                        sky_canyon_locations, techno_base_locations, egg_utopia_locations, xx_locations, SADV2Location
from Items import zone_table

class SADV2Region(Region):
    game: str = "Sonic Advance 2"

def create_regions(world: Multiworld, options: SADV2Options, player: int):
    menu_region = Region("Menu", player, world, "Zone Select")
    world.regions.append(menu_region)

    leaf_forest = create_region("Leaf Forest", player, world)
    create_locations(leaf_forest, leaf_forest_locations)
    connect(world, player, "Menu", "Leaf Forest", 
            lambda state: (state.has("Leaf Forest", player)))

    hot_crater = create_region("Hot Crater", player, world)
    create_locations(hot_crater, hot_crater_locations)
    connect(world, player, "Menu", "Hot Crater",
            lambda state: (state.has("Hot Crater", player)))

    music_plant = create_region("Music Plant", player, world)
    create_locations(music_plant, music_plant_locations)
    connect(world, player, "Menu", "Music Plant",
            lambda state: (state.has("Music Plant", player)))

    ice_paradise = create_region("Ice Paradise", player, world)
    create_locations(ice_paradise, ice_paradise_locations)
    connect(world, player, "Menu", "Ice Paradise",
            lambda state: (state.has("Ice Paradise", player)))

    sky_canyon = create_region("Sky Canyon", player, world)
    create_locations(sky_canyon, sky_canyon_locations)
    connect(world, player, "Menu", "Sky Canyon",
            lambda state: (state.has("Sky Canyon", player)))

    techno_base = create_region("Techno Base", player, world)
    create_locations(techno_base, techno_base_locations)
    connect(world, player, "Menu", "Techno Base",
            lambda state: (state.has("Techno Base", player)))

    egg_utopia = create_region("Egg Utopia", player, world)
    create_locations(egg_utopia, egg_utopia_locations)
    connect(world, player, "Menu", "Egg Utopia",
            lambda state: (state.has("Egg Utopia", player)))

    xx = create_region("XX", player, world)
    create_locations(xx, xx_locations)
    connect(world, player, "Menu", "XX",
            lambda state: (state.has("Red Chaos Emerald", player) and
                           state.has("Blue Chaos Emerald", player) and
                           state.has("Yellow Chaos Emerald", player) and
                           state.has("Green Chaos Emerald", player) and
                           state.has("White Chaos Emerald", player) and
                           state.has("Cyan Chaos Emerald", player) and
                           state.has("Purple Chaos Emerald")))



def create_region(name: str, player: int, world: Multiworld) -> SADV2Region:
    region = SADV2Region(name, player, world)
    world.region.append(region)

    return region

def create_locations(region: Region, *locations: dict):
    region.locations += [SADV2Location(region.player, location_name, locations[location_name], region) for location_name in locations]

def connect(world: Multiworld, player: int, outer_region: str, inner_region: str, \
            rule: typing.Optional[typing.Callable] = None):
    outer = world.get_region(outer_region)
    inner = world.get_region(inner_region)
    connection = Entrance(player, inner_region, outer)

    if rule:
        connection.access_rule = rule
    
    outer_region.exits.append(connection)
    connection.connect(inner)