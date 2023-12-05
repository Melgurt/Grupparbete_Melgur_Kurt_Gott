import random

class Villain:
    def __init__(self):
        self.hp = 1
        self.strengh = random.randint(1, 19)

    def villain_take_hp(self, amount):
        self.hp -= amount