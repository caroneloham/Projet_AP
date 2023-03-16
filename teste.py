import re

# ouvrir le fichier texte pour lire les informations de l'utilisateur
with open('Users/Marcq.Thibaud.txt', 'r') as f:
    # lire le contenu du fichier texte
    content = f.read()
    # extraire l'identifiant à l'aide d'une expression régulière
    match_username = re.search(r'Identifiant:\s*(\S+)', content)
    username = match_username.group(1)
    # extraire le mot de passe de la base de données à l'aide d'une expression régulière
    match_password = re.search(r'Mots_de_passe_bdd\s*:\s*(\S+)', content)
    password = match_password.group(1)

# afficher l'identifiant et le mot de passe extraits
print(f"Identifiant : {username}")
print(f"Mots de passe BDD : {password}")
