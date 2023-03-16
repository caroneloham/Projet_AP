import tkinter as tk
import subprocess
import random
import string
from pathlib import Path
import shutil

def generate_password():
    password = ''
    num_special_chars = random.randint(1, 2)
    num_digits = random.randint(3, 4)
    num_letters = random.randint(4, 20)

    # ajouter caractères spéciaux
    for i in range(num_special_chars):
        password += random.choice(string.punctuation)

    # ajouter chiffres
    for i in range(num_digits):
        password += random.choice(string.digits)

    # ajouter lettres
    for i in range(num_letters):
        password += random.choice(string.ascii_lowercase)

    # mélanger le mot de passe pour plus de sécurité
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password


def write_to_file():
    # Récupérer les informations saisies par l'utilisateur
    nom = nom_entry.get()
    prenom = prenom_entry.get()
    nom_domaine = nom_domaine_entry.get()

    # Créer le nom de fichier en utilisant le nom et le prénom de l'utilisateur
    nom_fichier = f"Users/{nom}.{prenom}.txt"
    fichier_existe = Path(nom_fichier).exists()
    if fichier_existe:
        confirmation_label.config(text="Le fichier existe déjà !")
        return

    # Écrire les informations dans le fichier
    with open(nom_fichier, "w") as file:
        file.write(f"Nom: {nom}\n")
        file.write(f"Prénom: {prenom}\n")
        file.write(f"Nom de domaine: {nom_domaine}\n")
    with open(nom_fichier, "a") as file:
        identifiant = f"{prenom[0]}.{nom}"
        file.write(f"Identifiant: {identifiant}\n")

    # Afficher un message de confirmation
    confirmation_label.config(text="Informations sauvegardées avec succès !")
    with open(nom_fichier, 'a') as file:
        # générer le mot de passe
        passwordftp = generate_password()
        passwordbdd = generate_password()
        passwordweb = generate_password()
        # écrire le mot de passe dans le fichier
        file.write("Mots_de_passe_ftp : " + passwordftp + "\n")
        file.write("Mots_de_passe_bdd : " + passwordbdd + "\n")
        file.write("Mots_de_passe_web : " + passwordweb + "\n")

    source_file = open(nom_fichier, "r")
    destination_file = open("Users/utilisateur.txt", "w")
    content = source_file.read()
    destination_file.write(content)
    source_file.close()
    destination_file.close()

# Créer la fenêtre principale
window = tk.Tk()
window.title("Créer un compte utilisateur")

# Créer les widgets pour saisir les informations
nom_label = tk.Label(window, text="Nom :")
nom_label.pack()
nom_entry = tk.Entry(window)
nom_entry.pack()

prenom_label = tk.Label(window, text="Prénom :")
prenom_label.pack()
prenom_entry = tk.Entry(window)
prenom_entry.pack()

nom_domaine_label = tk.Label(window, text="Nom de domaine :")
nom_domaine_label.pack()
nom_domaine_entry = tk.Entry(window)
nom_domaine_entry.pack()

# Créer le bouton de validation
valider_button = tk.Button(window, text="Valider", command=write_to_file)
valider_button.pack()

# Créer l'étiquette pour afficher le message de confirmation
confirmation_label = tk.Label(window)
confirmation_label.pack()

# Lancer la boucle principale de l'interface graphique
window.mainloop()
