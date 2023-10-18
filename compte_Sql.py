import pymysql
import re

# Connexion BDD
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='mot_de_passe_root'
)

# Open
with open('Users/utilisateur.txt', 'r') as f:
    content = f.read()
    match_username = re.search(r'Identifiant:\s*(\S+)', content)
    username = match_username.group(1)
    match_password = re.search(r'Mots_de_passe_bdd\s*:\s*(\S+)', content)
    password = match_password.group(1)
#edi de la base
with conn.cursor() as cursor:
    cursor.execute(f"CREATE DATABASE `{username}`;")
    cursor.execute(f"USE `{username}`;")
    cursor.execute(f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}';")
    cursor.execute(f"GRANT ALL PRIVILEGES ON `{username}`.* TO '{username}'@'localhost';")

conn.commit()

conn.close()

print(f"Identifiant : {username}")
print(f"Mots de passe BDD : {password}")
