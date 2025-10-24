from dataclasses import dataclass

from Options import Choice, PerGameCommonOptions

class StartingZone(Choice):
    """
    Determines with zone to start with. 
    Leaf Forest through Egg Utopia are valid along with random.
    """

    display_name = "Starting Zone"
    option_leaf_forest = 0
    option_hot_crater = 1
    option_music_plant = 2
    option_ice_paradise = 3
    option_sky_canyon = 4
    option_techno_base = 5
    option_egg_utopia = 6

    default = option_leaf_forest

@dataclass
class SADV2Options(PerGameCommonOptions):
    starting_zone: StartingZone