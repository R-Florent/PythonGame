from classPlayer import Player
from classWeapon import Weapon
from classMostre import mostre

knife = Weapon ("Couteau",3)
def main():
    print("hello wrold")

    player1 = Player("Joueur 1", 100, 20)
    player2 = Player("Joueur 2", 120, 15)

    # Exemple d'attaque
    player1.deal_damage(player2)


if __name__ == '__main__':
    main()
