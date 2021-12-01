from enum import Enum
import random

class Item(Enum):
    TREASURE = 0,
    MONSTER = 1,
    EMPTY = 2

class Room:
    def __init__(self, description):
        self.description = description
        self.items = []
        self.populate_items()

    def populate_items(self):
        enum_list = list(Item)
        self.items.append(random.choice(enum_list))
        self.items.append(random.choice(enum_list))
        self.items.append(random.choice(enum_list))