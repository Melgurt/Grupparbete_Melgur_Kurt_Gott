import random

class Player:
    def __init__(self, hp, level):
        self.strength = random.randint(1,21)
        self.hp = hp 
        self.inventory = []
        self.level = level

    def player_take_hp(self, amount):
        self.hp -= amount

    def fill_inventory(self, item):
        self.inventory.append(item)