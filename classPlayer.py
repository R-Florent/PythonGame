class Entity:
    def __init__(self, name, health, attack):
        self.name = name
        self._health = health
        self._attack = attack

    def get_health(self):
        return self._health

    def set_health(self, new_health):
        if new_health >= 0:
            self._health = new_health
        else:
            print("La valeur de santé doit être supérieure ou égale à zéro.")

    def get_attack(self):
        return self._attack

    def set_attack(self, new_attack):
        if new_attack >= 0:
            self._attack = new_attack
        else:
            print("La valeur d'attaque doit être supérieure ou égale à zéro.")

    def take_damage(self, damage):
        self.health -= damage
        print(self.pseudo, "a subi", damage, "points de dégâts.")
        if self.health <= 0:
            print(self.pseudo, "a été vaincu !")

    def deal_damage(self, target_player):
        target_player.take_damage(self.attack)
        print(self.pseudo, "inflige", self.attack, "points de dégâts à", target_player.pseudo)

    def attack_player(self, target_player):
        damage = self.attack

        # si le joueur a une arme
        if self.has_weapon():
            # ajoute les dégats de l'arme au point d'attaque du joueur
            damage += self.weapon.get_damage_amount()

        target_player.damage(damage)


class Player (Entity):

    def __init__(self, pseudo, health, attack, name):
        super().__init__(name, health, attack)
        self.weapon = None
        print ("Bienvenue au joueur ", pseudo,"Point de vie",health,"Attack", attack)


    # méthode pour changer l'arme du joueur
    def set_weapon(self, weapon):
        self.weapon = weapon

    # méthode pour verifier si le joueur a une arme
    def has_weapon(self):
        return self.weapon is not None

class Magicienn (Player, Entity) :

class gerrie (Player, Entity) :
class monstre (Entity):
