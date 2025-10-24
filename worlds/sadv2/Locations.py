from BaseClasses import Location

class SADV2Location(Location):
    game: str = "Sonic Advance 2"

leaf_forest_locations = {
    "Sonic - Leaf Forest Act 1": 0x10000,
    "Sonic - Leaf Forest Act 2": 0x10010,
    "Sonic - Leaf Forest Boss Act": 0x10020,

}

hot_crater_locations = {
    "Sonic - Hot Crater Act 1": 0x10040,
    "Sonic - Hot Crater Act 2": 0x10050,
    "Sonic - Hot Crater Boss Act": 0x10060,
}

music_plant_locations = {
    "Sonic - Music Plant Act 1": 0x10080,
    "Sonic - Music Plant Act 2": 0x10090,
    "Sonic - Music Plant Boss Act": 0x100a0,
}

ice_paradise_locations = {
    "Sonic - Ice Paradise Act 1": 0x100c0,
    "Sonic - Ice Paradise Act 2": 0x100d0,
    "Sonic - Ice Paradise Boss Act": 0x100e0,
}

sky_canyon_locations = {
    "Sonic - Sky Canyon Act 1": 0x10100,
    "Sonic - Sky Canyon Act 2": 0x10110,
    "Sonic - Sky Canyon Boss Act": 0x10120,
}

techno_base_locations = {
    "Sonic - Techno Base Act 1": 0x10140,
    "Sonic - Techno Base Act 2": 0x10150,
    "Sonic - Techno Base Boss Act": 0x10160,
}

egg_utopia_locations = {
    "Sonic - Egg Utopia Act 1": 0x10180,
    "Sonic - Egg Utopia Act 2": 0x10190,
    "Sonic - Egg Utopia Boss Act": 0x101a0,
}

xx_locations = {
    "Sonic - XX": 0x101c0,
}

event_locations = {
    "True Area 53": None
}

all_locations = {
    **leaf_forest_locations,
    **hot_crater_locations,
    **music_plant_locations,
    **ice_paradise_locations,
    **sky_canyon_locations,
    **techno_base_locations,
    **egg_utopia_locations,
    **xx_locations
}