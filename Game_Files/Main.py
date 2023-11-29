import random
health_points = 10
strength = 10
level = 1
inventory = [""]

class item:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength
class player:
    def __init__(self, strength, hp, inventory, level):
        self.strength = strength
        self.hp = hp 
        self.inventory = inventory
        self.level = level

    def take_hp(amount):
        self.hp -= amount

def sum_strength_comparison(playerstrength, monsterstrength):
    sum_playerstrength = strength + item.strength
    monsterstrength = random.randint(1, 21)
#vi ska göra till klass


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


