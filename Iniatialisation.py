# 1.Importez les bibliothèques nécessaires
import tkinter as tk
import random

# 2.Initialisez la fenêtre de jeu avec les dimensions et le titre appropriés
fenetre = tk.Tk()
fenetre.geometry("400x300")
fenetre.title("Pierre-Papier-Ciseaux")

# 3.Définisez la couleur d'arrière-plan de la fenêtre
fenetre.configure(bg="#f0f8ff")

# 4.Créez une étiquette pour le titre du jeu et affichez-la
label_titre = tk.Label(fenetre, text="Jeu Pierre-Papier-Ciseaux", font=("Arial", 16), bg="#f0f8ff")
label_titre.grid(row=0, column=0, columnspan=2, pady=10)

# 5.Demandez à l'utilisateur de choisir entre Pierre, Papier ou Ciseaux
var_choix = tk.StringVar()

# 6.Créez un champ de saisie pour que l'utlisateur puisse saisir son choix
label_choix = tk.Frame(fenetre, bg="#f0f8ff")
label_choix.grid(row=1, column=0, padx=10, pady=10)
tk.Label(label_choix, text="Choisissez entre (Pierre-Papier-Ciseaux)", bg="#f0f8ff").pack(side='left', padx=5)
tk.Entry(label_choix, textvariable=var_choix.get(), width=20, bg="white").pack(side='left', pady=5)

# 7.Générez un choix aléatoire pour l'ordinateur (Pierre, Papier ou Ciseaux)
choix_ordi = random.choice(["Pierre", "Papier", "Ciseaux"])

# 8.Affectez la sélection générée aléatoirement à une variable comp_pick
comp_pick = choix_ordi

fenetre.mainloop()