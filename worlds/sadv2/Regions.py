from BaseClasses import Region, Multiworld, Location
from Locations import leaf_forest_locations, hot_crater_locations, music_plant_locations, ice_paradise_locations, \
                        sky_canyon_locations, techno_base_locations, egg_utopia_locations, xx_locations, SADV2Location

class SADV2Region(Region):
    game: str = "Sonic Advance 2"

def create_regions(world: Multiworld, options: SADV2Options, player: int):
    menu_region = Region("Menu", player, world, "Zone Select")
    world.regions.append(menu_region)

    leaf_forest = create_region("Leaf Forest", player, world)
    create_locations(leaf_forest, leaf_forest_locations)

    hot_crater = create_region("Hot Crater", player, world)
    create_locations(hot_crater, hot_crater_locations)

    music_plant = create_region("Music Plant", player, world)
    create_locations(music_plant, music_plant_locations)

    ice_paradise = create_region("Ice Paradise", player, world)
    create_locations(ice_paradise, ice_paradise_locations)

    sky_canyon = create_region("Sky Canyon", player, world)
    create_locations(sky_canyon, sky_canyon_locations)

    techno_base = create_region("Techno Base", player, world)
    create_locations(techno_base, techno_base_locations)

    egg_utopia = create_region("Egg Utopia", player, world)
    create_locations(egg_utopia, egg_utopia_locations)

    xx = create_region("XX", player, world)
    create_locations(xx, xx_locations)



def create_region(name: str, player: int, world: Multiworld) -> SADV2Region:
    region = SADV2Region(name, player, world)
    world.region.append(region)

    return region

def create_locations(region: Region, *locations: dict):
    region.locations += [SADV2Location(region.player, location_name, locations[location_name], region) for location_name in locations]