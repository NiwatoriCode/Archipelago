import typing

from BaseClasses import Item, ItemClassification

class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: int
    event: bool = False

class SADV2Item(Item):
    game: str = "Sonic Advance 2"

    def __init__(self, name, classification: ItemClassification, code: int = None, player: int = None):
        super(SADV2Item, self).__init__(name, classification, code, player)

character_table = {
    "Sonic Rescued": ItemData(100, 1)
}

zone_table = {
    "Leaf Forest": ItemData(200, 1),
    "Hot Crater": ItemData(201, 1),
    "Music Plant": ItemData(202, 1),
    "Ice Paradise": ItemData(203, 1),
    "Sky Canyon": ItemData(204, 1),
    "Techno Base": ItemData(205, 1),
    "Egg Utopia": ItemData(206, 1)
}

emerald_table = {
    "Red Chaos Emerald": ItemData(300, 2),
    "Blue Chaos Emerald": ItemData(301, 2),
    "Yellow Chaos Emerald": ItemData(302, 2),
    "Green Chaos Emerald": ItemData(303, 2),
    "White Chaos Emerald": ItemData(304, 2),
    "Cyan Chaos Emerald": ItemData(305, 2),
    "Purple Chaos Emerald": ItemData(306, 2)
}

filler_table = {
    "Cheat Code to Unlock Shadow": ItemData(400, 0),
    "The Other Half of the Moon": ItemData(401, 0),
    "Love Letter From Vector": ItemData(402, 0),
    "Computer Room": ItemData(403, 0),
    "Huge Chao Garden": ItemData(404, 0),
    "Scratch and Grounder": ItemData(405, 0),
    "Bocoe and Decoe": ItemData(406, 0),
    "Orbot and Cubot": ItemData(407, 0),
    "Phantom Ruby": ItemData(408, 0),
    "Every Single Drop of All You've Got": ItemData(409, 0)
}

event_table = {
    "XX Coordinates 1": ItemData(None, 1, True),
    "XX Coordinates 2": ItemData(None, 1, True),
    "XX Coordinates 3": ItemData(None, 1, True),
    "XX Coordinates 4": ItemData(None, 1, True),
    "XX Coordinates 5": ItemData(None, 1, True),
    "XX Coordinates 6": ItemData(None, 1, True),
    "XX Coordinates 7": ItemData(None, 1, True),
    "Vanilla Rescued": ItemData(None, 1, True)
}

item_table = {
    **character_table,
    **zone_table,
    **emerald_table,
    **filler_table
}