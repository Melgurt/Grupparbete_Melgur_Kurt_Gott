class Player:
    def __init__(self, strength, hp, level):
        self.strength = strength
        self.hp = hp 
        self.inventory = []
        self.level = level

        def player_take_hp(amount):
            self.hp -= amount

        def fill_inventory(item):
            self.inventory.append(item)