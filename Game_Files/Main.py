import random
from player import Player
from villain import Villain
from item import Item
from battle import battle

player1 = Player(5, 1)
auto_weapon = Item("Fists")
player1.fill_inventory(auto_weapon)

def list_print(list):
    for i in range(len(player1.inventory)):
        for f in player1.inventory:
            print(i + 1, ", ", f.name)


print("I don't care to write any story blöblböblöbblöbl")
print("You are granted with a choice where you can choose two paths. Please enter right or left")

while True:
    
    first_choice = input(">")
    
    if(first_choice == "right"):
        
        print("You chose right")
        print("You enterd a room with a chest")
        
        weapon_first_choice = Item("Knuckle-duster")
        
        print(f"You foudnd chest, inside the chest {weapon_first_choice.name}")
        print("Do you want to take this weapon?")
        
        yes_or_no_weapon = input("yes/no -> ")

        if(yes_or_no_weapon == "yes"):
            
            print("You chose to take the weapon")
            print("What invetory place do you want the item to be, please enter a number 1-5")

            invetory_slot_choice = int(input("> ")) - 1

            player1.fill_inventory(weapon_first_choice, invetory_slot_choice)
        
            break
        
        elif(yes_or_no_weapon == "no"):
        
            print("You chose not to take the weapon")
        
            break

        break

    elif (first_choice == "left"):
        
        print("You chose left")
        print("OAOOAOAWWW CRAAAP you enterd a room with a monster in it")
        print("What weapon you choose in your inventory?")
        list_print(player1.inventory)
        
        weapon_slot = int(input(">"))
        
        player1_weapon_compare = player1.inventory[weapon_slot-1]
        
        villain_first_choice= Villain()

        battle(player1, player1_weapon_compare, villain_first_choice)

        break

    print("Please enter right or left")
    


print("More story blölöblbölbölböl, hope no villain in next door.(You're gonna die)")


