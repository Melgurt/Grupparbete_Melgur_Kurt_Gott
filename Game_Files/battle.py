import random
from villain import Villain
from player import Player
from item import Item

def battle(player : Player, item: Item, villain: Villain):

    print(item.damage + player.strength)

    if item.damage + player.strength > villain.strenght:
        villain.villain_take_hp(1)
        print("YOu kill him")
        print(f"You leveel up {player.level} levels")
        player.player_levelup(1)
        print(f"Your level is now {player.level}")

    elif villain.strenght > item.damage + player.strength:
        player.player_take_hp(1)
        print("you take dmg")
        print(f"Your hp is now {player.hp}")
        

    else:
        print("You are equal in strength. It lets you pass and go on you weak wack")
