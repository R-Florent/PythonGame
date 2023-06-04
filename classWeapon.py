
class Weapon:

    def __init__(self, name=None, dmg=None):
        self.name = name
        self.damage = dmg

    def get_name(self):
        return self.name

    def get_damage_amount(self):
        return self.damage
