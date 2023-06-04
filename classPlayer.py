
class Player:

    def __init__(self, pseudo, health, attack, ):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print ("Bienvenue au joueur ", pseudo,"Point de vie",health,"Attack", attack)

    def get_pseudo(self):
        return self.pseudo

    def get_health (self):
        return self.health

    def get_attack_value(self):
        return self.attack

    def take_damage(self, damage):
        self.health -= damage
        print(self.pseudo, "a subi", damage, "points de dégâts.")
        if self.health <= 0:
            print(self.pseudo, "a été vaincu !")

    def deal_damage(self, target_player):
        target_player.take_damage(self.attack)
        print(self.pseudo, "inflige", self.attack, "points de dégâts à", target_player.pseudo)
