import pymysql
import re

# se connecter à la base de données
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='mot_de_passe_root'
)

# ouvrir le fichier texte pour lire les informations de l'utilisateur
with open('utilisateur.txt', 'r') as f:
    # lire le contenu du fichier texte
    content = f.read()
    # extraire l'identifiant à l'aide d'une expression régulière
    match_username = re.search(r'Identifiant:\s*(\S+)', content)
    username = match_username.group(1)
    # extraire le mot de passe de la base de données à l'aide d'une expression régulière
    match_password = re.search(r'Mots_de_passe_bdd\s*:\s*(\S+)', content)
    password = match_password.group(1)

# créer la base de données avec le nom d'utilisateur extrait
with conn.cursor() as cursor:
    cursor.execute(f"CREATE DATABASE `{username}`;")
    cursor.execute(f"USE `{username}`;")
    # créer un utilisateur avec les autorisations nécessaires dans la base de données
    cursor.execute(f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}';")
    # accorder toutes les autorisations à l'utilisateur sur la base de données portant son nom d'utilisateur
    cursor.execute(f"GRANT ALL PRIVILEGES ON `{username}`.* TO '{username}'@'localhost';")

# enregistrer les modifications dans la base de données
conn.commit()

# fermer la connexion à la base de données
conn.close()

# afficher l'identifiant et le mot de passe extraits
print(f"Identifiant : {username}")
print(f"Mots de passe BDD : {password}")
