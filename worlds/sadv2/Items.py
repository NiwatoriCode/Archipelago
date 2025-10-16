import typing

from BaseClasses import Item, ItemClassification

class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: bool
    event: bool = False

class SADV2Item(Item):
    game: str = "Sonic Advance 2"

character_table = {
    "Sonic Rescued": ItemData(100, True)
}

zone_table = {
    "Leaf Forest": ItemData(200, True),
    "Hot Crater": ItemData(201, True),
    "Music Plant": ItemData(202, True),
    "Ice Paradice": ItemData(203, True),
    "Sky Canyon": ItemData(204, True),
    "Techno Base": ItemData(205, True),
    "Egg Utopia": ItemData(206, True)
}

emerald_table = {
    "Red Chaos Emerald": ItemData(300, True),
    "Blue Chaos Emerald": ItemData(301, True),
    "Yellow Chaos Emerald": ItemData(302, True),
    "Green Chaos Emerald": ItemData(303, True),
    "White Chaos Emerald": ItemData(304, True),
    "Cyan Chaos Emerald": ItemData(305, True),
    "Purple Chaos Emerald": ItemData(306, True)
}

filler_table = {
    "Cheat Code to Unlock Shadow": ItemData(400, False),
    "The Other Half of the Moon": ItemData(401, False),
    "Love Letter From Vector": ItemData(402, False),
    "Computer Room": ItemData(403, False),
    "Huge Chao Garden": ItemData(404, False),
    "Scratch and Grounder": ItemData(405, False),
    "Bocoe and Decoe": ItemData(406, False),
    "Orbot and Cubot": ItemData(407, False),
    "Phantom Ruby": ItemData(408, False),
    "Every Single Drop of All You've Got": ItemData(409, False)
}

event_table = {
    "XX Coordinates 1": ItemData(None, True, True),
    "XX Coordinates 2": ItemData(None, True, True),
    "XX Coordinates 3": ItemData(None, True, True),
    "XX Coordinates 4": ItemData(None, True, True),
    "XX Coordinates 5": ItemData(None, True, True),
    "XX Coordinates 6": ItemData(None, True, True),
    "XX Coordinates 7": ItemData(None, True, True),
    "Vanilla Rescued": ItemData(None, True, True)
}