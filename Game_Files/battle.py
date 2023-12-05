import random
from villain import Villain
from player import Player
from item import Item

class Battle:
    def __init__(self, player : Player, item: Item, villain: Villain):
        if item.damage >= villain.strengh:
            villain.villain_take_hp(item.damage)
        else:
            player.player_take_hp(villain.strengh)