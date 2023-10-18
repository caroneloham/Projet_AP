import re
from pyftpdlib.authorizers import UnixAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# On recupére les informations
with open('Users/caron.eloham.txt', 'r') as f:
    content = f.read()
    match_username = re.search(r'Identifiant:\s*(\S+)', content)
    username = match_username.group(1)
    match_password = re.search(r'Mot_de_passe_ftp:\s*(\S+)', content)
    password = match_password.group(1)

authorizer = UnixAuthorizer()

# Ajouter un utilisateur avec un mot de passe
homedir = "/chemin/vers/le/repertoire/racine"
perm = "elradfmwMT"  
authorizer.add_user(username, password, homedir, perm=perm)

handler = FTPHandler
handler.authorizer = authorizer

address = ("", 21)
server = FTPServer(address, handler)

server.serve_forever()
