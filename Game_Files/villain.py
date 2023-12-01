class Villain:
    def __init__(self, hp, strength):
        self.hp = hp
        self.strength = strength

        def villain_take_hp(amount):
            self.hp -= amount