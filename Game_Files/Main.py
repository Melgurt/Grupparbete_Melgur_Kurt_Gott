import random
health_points = 10
strength = 10
level = 1
inventory = [""]

class Item:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
class Player:
    def __init__(self, strength, hp, level):
        self.strength = strength
        self.hp = hp 
        self.inventory = []
        self.level = level

        def player_take_hp(amount):
            self.hp -= amount

        def fill_inventory(item: Item):
            self.inventory.append(item)

class Villain:
    def __init__(self, hp, strength):
        self.hp = hp
        self.strength = strength

        def villain_take_hp(amount):
            self.hp -= amount

print("story blalal")

print("You are granted with a choice where you can choose two paths. Please enter right or left")
first_choice = input(">")

if(first_choice == "right"):
    print("You chose right")

elif (first_choice == "left"):
    print("You chose left")

else:
    print("Please enter right or left")

print("More story bblblbl")


