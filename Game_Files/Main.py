import random
import sys


    
class Item:
    def __init__(self, name):
        self.name = name
        self.damage = random.randint(1, 21)

class Player:
    def __init__(self, hp, level):
        self.strength = 5
        self.hp = hp 
        self.inventory = []
        self.level = level

    def player_levelup(self, amount):
        self.level += amount

    def player_take_hp(self, amount):
        self.hp -= amount

    def fill_inventory(self, item):
        self.inventory.append(item)
    
    def delete_inventory(self, index):
        self.inventory.pop(index - 1)

    def player_death(self, hp, level):
        self.strength = 5
        self.hp = hp
        self.level = level
        self.inventory = []

class Villain:
    def __init__(self):
        self.hp = 1
        self.strength = random.randint(1, 19)

    def villain_take_hp(self, amount):
        self.hp -= amount



def battle(player : Player, item: Item, villain: Villain):

    print(f"Your damage-> {item.damage + player.strength}")
    print(f"Villain damage-> {villain.strength}")

    if item.damage + player.strength > villain.strength:
        villain.villain_take_hp(1)
        print("YOu kill him")
        print(f"You leveel up {player.level} levels")
        player.player_levelup(1)
        print(f"Your level is now {player.level}")

    elif villain.strength > item.damage + player.strength:
        player.player_take_hp(1)
        print("you take dmg")
        print(f"Your hp is now {player.hp}")
        

    else:
        print("You are equal in strength. It lets you pass and go on you weak wack")



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
        while True:
            if player1.hp <= 0:

                retry_input = 0
                print("YOU HAVE DIED")
                player1.player_death(5, 1)
                auto_weapon = Item("Fists")
                player1.fill_inventory(auto_weapon)

                print("Do you want to retry?")
                retry_input = input("yes/(any input) -> ")

                if retry_input != "yes":
                    sys.exit()

                    
        
            elif player1.level >= 10:

                retry_input = 0
                player1.player_death(5, 1)
                auto_weapon = Item("Fists")
                player1.fill_inventory(auto_weapon)

                
                for _ in range(0, 10):
                    print("YOU HAVE WON")
                print("Do you want to play again?")
                retry_input = input("yes/(any input) -> ")

                if retry_input != "yes":
                    sys.exit()

            else:
                break


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
        print(f"Item {player1.inventory.index(f)+1}, {f.name}, {f.damage} damage")
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

    weapon = Item(weapon_list[random.randint(0, 15)])
    print(f"In the chest is {weapon.name}")

    print("Do you want to take this weapon?")

    yes_or_no_weapon = input("yes/no -> ")

    while True:
        
        if yes_or_no_weapon == "yes" or yes_or_no_weapon == "no":
            break
        else:
            print(f""" 
                                     
Something went wrong, you put in "{yes_or_no_weapon}"
Retry putting in yes or no, not in capitals
""") 
        yes_or_no_weapon = input("yes/no -> ")

    while True:
        if(yes_or_no_weapon == "yes"):
            
            print("You chose to take the weapon")

            if len(player1.inventory) > 4:
                print("You have too many items in inventory")
                print(f"Which weapon do you want to throw away?")
                list_print()

                while True:
                    try:
                        weapon_delete_index = int(input("-> "))
                        for i in range(1, len(player1.inventory) + 1):
                            if weapon_delete_index == i:
                                break
                        break
                    except ValueError:
                        print("Choose a valid number from the list")
                        list_print()

                        
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
        

    
    while True:
        try:
            chosen_weapon = input("-> ")
            chosen_weapon = int(chosen_weapon)

            for i in range(1, len(player1.inventory)+1):
                if chosen_weapon == i:
                    break

            try:
                player1_weapon_compare = player1.inventory[chosen_weapon-1]

            except IndexError:
                print("Yu can not choose that number") 

            villain_first_choice= Villain()
            battle(player1, player1_weapon_compare, villain_first_choice) 
            break 

        except ValueError:
            print(f"""

Something went wrong, you put in "{chosen_weapon}"
Retry putting in one of the numbers
""")
        except:
            print(f"You have put in wrong input")

menu()





