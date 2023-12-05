import random

class Item:
    def __init__(self, name):
        self.name = name
        self.damage = random.randint(1, 21)