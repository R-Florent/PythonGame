from classPlayer import Player
from classWeapon import Weapon
# from classMostre import mostre


def main():
    print("hello wrold")

    knife = Weapon("Couteau", 3)
    player1 = Player("Joueur 1", 100, 20)
    player2 = Player("Joueur 2", 120, 15)
    print(player2.name)
    # Exemple d'attaque
    player1.deal_damage(player2)


if __name__ == '__main__':
    main()
