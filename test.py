from tkinter import *

window = Tk()

window.title("My Appliocation")

window.mainloop()
window.geometry("1080x720")

"""
from classPlayer import Player

def attack_player():
    player1.deal_damage(player2)
    update_health_labels()

def update_health_labels():
    health_label1.config(text=f"Vie du Joueur 1 : {player1.get_health()}")
    health_label2.config(text=f"Vie du Joueur 2 : {player2.get_health()}")

root = tk.Tk()
root.title("Bataille des joueurs")

# Création des joueurs
player1 = Player("Joueur 1", 100, 20)
player2 = Player("Joueur 2", 120, 15)

# Création des widgets
title_label = tk.Label(root, text="Bataille des joueurs", font=("Helvetica", 16, "bold"))
health_label1 = tk.Label(root, text=f"Vie du Joueur 1 : {player1.get_health()}")
health_label2 = tk.Label(root, text=f"Vie du Joueur 2 : {player2.get_health()}")
attack_button = tk.Button(root, text="Attaquer", command=attack_player)

# Placement des widgets dans la fenêtre
title_label.pack()
health_label1.pack()
health_label2.pack()
attack_button.pack()

root.mainloop()
"""