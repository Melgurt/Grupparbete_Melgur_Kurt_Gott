import random
from villain import Villain
from player import Player
from item import Item

def battle(player : Player, item: Item, villain: Villain):

    print(f"Which weapon do you want to use?: {player.inventory}")
    index_chosen_weapon = int(input(">")) - 1
    

    if index_chosen_weapon.damage > villain.strenght:
        villain.villain_take_hp(item.damage)
    elif villain.strenght > index_chosen_weapon.damage:
        player.player_take_hp(villain.strengh)
    else:
        print("You are equal in strength. It lets you pass and go on you weak wack")
