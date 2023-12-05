import random
from player import Player
from villain import Villain
from item import Item

player1 = Player()
print("I don't care to write any story blöblböblöbblöbl")

print("You are granted with a choice where you can choose two paths. Please enter right or left")

while True:
    first_choice = input(">")
    if(first_choice == "right"):
        print("You chose right")
        print("You enterd a room with a chest")
        break

    elif (first_choice == "left"):
        print("You chose left")
        print("OAOOAOAWWW CRAAAP you enterd a room with a monster in it")
        villain_first_choice= Villain()
        
        break

    print("Please enter right or left")


print("More story blölöblbölbölböl")


