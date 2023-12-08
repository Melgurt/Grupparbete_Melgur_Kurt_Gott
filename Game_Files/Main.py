import random
from player import Player
from villain import Villain
from item import Item
from battle import battle
import sys


player1 = Player(5, 1)
auto_weapon = Item("Fists")
player1.fill_inventory(auto_weapon)
weapon_list = ["Battle Axe", "Club", "Flail", "Mace", "War Hammer", "Dagger", "Katana", "Longsword", "Rapier", "Shortsword", "Lance", "Pike", "Spear", "War Scythe", "Swordstaff", "Knuckle-Dusters"]

def menu():
    while True:

        print("1 , Play game    2 , Close game")
        print("Choose")
        
        menu_choice = input("-> ")
        
        if menu_choice == "1":
            game()

        elif menu_choice == "2":
            sys.exit()

        else:
            print("Choose 1 or 2")
    

def game():
    while True:

        if player1.hp <= 0:
            print("YOU HAVE DIED")
            player1.player_death()
            auto_weapon = Item("Fists")
            player1.fill_inventory(auto_weapon)

            print("Do you want to retry?")
            retry_input = input("yes/any input -> ")

            if retry_input == "yes":
                game()
                break

            else:
                sys.exit()
        
        elif player1.level >= 10:
            for i in range(0, 10):
                print("YOU HAVE WON")

        else:
            pass


        print("1. Story    2. Inventory    3. Stats    4. Exit Game")
        choice = input("-> ")

        if choice == "1":
            print("I don't care to write any story blöblböblöbblöbl")
            print("You are granted with a choice where you can choose three paths. Please enter right, left or forward")
            chosen_path = 0
            chosen_path = input("-> ")

            while True:
                if chosen_path == "left":
                    print("You chose left, story, story, story")
                    random_story()
                    break
        
                elif chosen_path == "right":
                    print("You chose right, sroty story story")
                    random_story()
                    break
        
                elif chosen_path == "forward":
                    print("You chose forward, story story storyr")
                    random_story()
                    break
                
                else:
                    print("You went back to menu for writing something else than forward, left or right")
                    break

        elif choice == "2":
            list_print()
            
        
        elif choice == "3":
            print("Stats:")

            print(f"You have {player1.hp}hp")
            print(f"You are level {player1.level}")
            print(f"You have {player1.strength} strength")

            print("------------------------------------")
            
        
        elif choice == "4":
            sys.exit()
        
        else:
            print("Choose 1, 2, 3 or 4")
        

def list_print():

    print("Inventory:")
    for f in player1.inventory:
        print(f"Item {player1.inventory.index(f)+1}, {f.name}")
    print("-----------------------------------------------")

            
def random_story():
    print("Böböböb")
    i = random.randint(0, 2)
    if i == 0:
        chest_room()
    elif i == 1:
        villain_room()
    elif i == 2:
        trap_room()



def chest_room():

    for _ in range(0, 6):
        print("")
    print("_________________________________________________________________")

    print("You entered a room with a chest and opened it")

    weapon = Item(weapon_list[random.randint(0, 16)])
    print(f"In the chest is {weapon.name}")

    print("Do you want to take this weapon?")

    while True:
        yes_or_no_weapon = input("yes/no -> ")
        if yes_or_no_weapon == "yes" or yes_or_no_weapon == "no":
            break
        else:
            yes_or_no_weapon = print(f""" 
                                     
Something went wrong, you put in "{yes_or_no_weapon}"
Retry putting in yes or no, not in capitals
""")

    


    while True:
        if(yes_or_no_weapon == "yes"):
            
            print("You chose to take the weapon")

            if len(player1.inventory) > 4:
                print("You have too many items in inventory")
                print(f"Which weapon do you want to throw away?")
                list_print()

                weapon_delete_index = int(input("-> "))

                while True:
                    if not weapon_delete_index is int:            # GÖR SÅDANA HÄR KANSKE PÅ STÄLLEN       FIXA EXCEPTIONS OCH VINST OCH DÖD
                        print("Please enter a valid NUMBER")
                        weapon_delete_index = int(input("-> "))
                    elif weapon_delete_index is int:
                        break
                        
                player1.delete_inventory(weapon_delete_index)
                player1.fill_inventory(weapon)
                break
        
            else:
                player1.fill_inventory(weapon)
                break

        elif(yes_or_no_weapon == "no"):
        
            print("You chose not to take the weapon")
            break

        else:
            print("You gave the wrong input, now you are in the menu, yes/no means yes or no")
            break

def trap_room():
    for _ in range(0, 6):
        print("")
    print("_________________________________________________________________")

    print("Oh no! you have stepped into a trap")

    damage_taken = random.randint(0, 4)
    print(f"You have lost {damage_taken}hp")

    player1.player_take_hp(damage_taken)

    print(f"You now have {player1.hp}hp")

def villain_room():

    for _ in range(0, 6):
        print("")
    print("_________________________________________________________________")

    print("OAOOAOAWWW CRAAAP you enterd a room with a monster in it")
    print("What weapon you choose in your inventory?")
    
    list_print()
        
    weapon_slot = input(">")

    
    while True:
        try:
            int(weapon_slot)
        except:
            pass
        
        if weapon_slot is int:
            for i in range(1, len(player1.inventory)+1):

                if weapon_slot == i:
                    break
        
        else:
            print(f"""

Something went wrong, you put in "{weapon_slot}"
Retry putting in one of the numbers
""")
            weapon_slot = input("->")
        
    player1_weapon_compare = player1.inventory[weapon_slot-1]
        
    villain_first_choice= Villain()

    battle(player1, player1_weapon_compare, villain_first_choice)    

menu()

# while True:
    
#     first_choice = input(">")
    
#     if(first_choice == "right"):
        
#         print("You chose right")
#         print("You enterd a room with a chest")
        
#         weapon_first_choice = Item("Knuckle-duster")
        
#         print(f"You foudnd chest, inside the chest {weapon_first_choice.name}")
#         print("Do you want to take this weapon?")
        
#         yes_or_no_weapon = input("yes/no -> ")

#         if(yes_or_no_weapon == "yes"):
            
#             print("You chose to take the weapon")
#             print("What invetory place do you want the item to be, please enter a number 1-5")

#             invetory_slot_choice = int(input("> ")) - 1

#             player1.fill_inventory(weapon_first_choice)
        
#             break
        
#         elif(yes_or_no_weapon == "no"):
        
#             print("You chose not to take the weapon")
        
#             break

#         break

#     elif (first_choice == "left"):
        
#         print("You chose left")
#         print("OAOOAOAWWW CRAAAP you enterd a room with a monster in it")
#         print("What weapon you choose in your inventory?")
#         list_print(player1.inventory)
        
#         weapon_slot = int(input(">"))
        
#         player1_weapon_compare = player1.inventory[weapon_slot-1]
        
#         villain_first_choice= Villain()

#         battle(player1, player1_weapon_compare, villain_first_choice)

#         break

#     elif (first_choice == "forward"):
#         print("You went through a trap")
#         print("You lost 1 hp")
#         player1.player_take_hp(1)

#     print("Please enter right or left")
    


# print("More story blölöblbölbölböl, hope no villain in next door you choose.(You're gonna die)")
# print("Choose next path: left, right or forward")

# while True:
#     second_choice = input("-> ")
    
#     if(second_choice == "right"):
        
#         print("You chose right")
#         print("You enterd a room with a chest")
        
#         weapon_second_choice = Item("")
        
#         print(f"You foudnd chest, inside the chest {weapon_second_choice.name}")
#         print("Do you want to take this weapon?")
        
#         yes_or_no_weapon = input("yes/no -> ")

#         if(yes_or_no_weapon == "yes"):
            
#             print("You chose to take the weapon")
#             print("What invetory place do you want the item to be, please enter a number 1-5")

#             invetory_slot_choice = int(input("> ")) - 1

#             player1.fill_inventory(weapon_first_choice)
        
#             break
        
#         elif(yes_or_no_weapon == "no"):
        
#             print("You chose not to take the weapon")
        
#             break

#         break

#     elif (second_choice == "left"):
        
#         print("You chose left")
#         print("OAOOAOAWWW CRAAAP you enterd a room with a monster in it")
#         print("What weapon you choose in your inventory?")
#         list_print(player1.inventory)
        
#         weapon_slot = int(input(">"))
        
#         player1_weapon_compare = player1.inventory[weapon_slot-1]
        
#         villain_first_choice= Villain()

#         battle(player1, player1_weapon_compare, villain_first_choice)

#         break

#     elif (second_choice == "forward"):
#         print("You went through a gas trap")
#         print("You lost 1 hp")
#         player1.player_take_hp(1)

#     print("Please enter right or left")
    




