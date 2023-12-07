import random

class Player:
    def __init__(self, hp, level):
        self.strength = 5
        self.hp = hp 
        self.inventory = []
        self.level = 1

    def player_levelup(self, amount):
        self.level += amount

    def player_take_hp(self, amount):
        self.hp -= amount

    def fill_inventory(self, item):
        self.inventory.append(item)
    
    def delete_inventory(self, index):
        self.inventory.pop(index - 1)