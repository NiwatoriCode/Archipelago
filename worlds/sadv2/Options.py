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

class StartingCharacter(Choice):
    """
    Determines which character to start with.
    Sonic must be available for goal.
    If yaml settings cause Sonic to not be available, one character will be replaced with Sonic.
    """

    display_name = "Starting Character"
    option_sonic = 0
    option_cream = 1
    option_tails = 2
    option_knuckles = 3
    option_amy = 4

    default = option_sonic

@dataclass
class SADV2Options(PerGameCommonOptions):
    starting_zone: StartingZone
    starting_character: StartingCharacter