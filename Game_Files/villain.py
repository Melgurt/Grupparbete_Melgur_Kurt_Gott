import random

class Villain:
    def __init__(self):
        self.hp = 1
        self.strenght = random.randint(1, 19)

    def villain_take_hp(self, amount):
        self.hp -= amount