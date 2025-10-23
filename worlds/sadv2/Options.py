from Options import Choice, PreGameOptions

class StartingZone(Choice):
    """
    Determines with zone to start with. 
    Leaf Forest through Egg Utopia are valid along with random.
    """

    display_name = "Starting Zone"
    leaf_forest = 0
    hot_crater = 1
    music_plant = 2
    ice_paradise = 3
    sky_canyon = 4
    techno_base = 5
    egg_utopia = 6

class SADV2Options(PreGameOptions):
    starting_zone: StartingZone