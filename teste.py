import re

with open('Users/utilisateur.txt', 'r') as f:
    content = f.read()
    match_username = re.search(r'Identifiant:\s*(\S+)', content)
    username = match_username.group(1)
    match_password = re.search(r'Mots_de_passe_bdd\s*:\s*(\S+)', content)
    password = match_password.group(1)


print(f"Identifiant : {username}")
print(f"Mots de passe BDD : {password}")
