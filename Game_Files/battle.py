import random
from villain import Villain
from player import Player
from item import Item

def battle(player : Player, item: Item, villain: Villain):
    print(f"ur damage {item.damage} vs enemy damage {villain.strenght}")
    if item.damage > villain.strenght:
        villain.villain_take_hp(1)
        print("YOU SLASH HIS LITTLEFIGGER OFF AND HE GOD IE")
    elif villain.strenght > item.damage:
        player.player_take_hp(1)
        print("LMFAO U DEADASSDEAD")
    else:
        print("You are equal in strength. It lets you pass and go on you weak wack")
