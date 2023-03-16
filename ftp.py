import re
from pyftpdlib.authorizers import UnixAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Ouvrir le fichier texte pour lire les informations de l'utilisateur
with open('Users/caron.eloham.txt', 'r') as f:
    # Lire le contenu du fichier texte
    content = f.read()
    # Extraire l'identifiant à l'aide d'une expression régulière
    match_username = re.search(r'Identifiant:\s*(\S+)', content)
    username = match_username.group(1)
    # Extraire le mot de passe de la base de données à l'aide d'une expression régulière
    match_password = re.search(r'Mot_de_passe_ftp:\s*(\S+)', content)
    password = match_password.group(1)

# Créer un objet UnixAuthorizer pour gérer les utilisateurs
authorizer = UnixAuthorizer()

# Ajouter un utilisateur avec un mot de passe
homedir = "/chemin/vers/le/repertoire/racine"
perm = "elradfmwMT"  # Permissions pour l'utilisateur (optionnel)
authorizer.add_user(username, password, homedir, perm=perm)

# Créer un objet FTPHandler pour gérer les connexions FTP
handler = FTPHandler
handler.authorizer = authorizer

# Créer un objet FTPServer pour gérer le serveur FTP
address = ("", 21)
server = FTPServer(address, handler)

# Lancer le serveur FTP
server.serve_forever()
