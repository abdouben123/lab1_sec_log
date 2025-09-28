from dotenv import load_dotenv
import os

# Charger les variables du fichier .env
load_dotenv()

# Récupérer les secrets
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
api_key = os.getenv("API_KEY")

# Exemple simple : utilisation des secrets
print("Connexion à la base de données avec :")
print(f"Utilisateur : {db_user}")
print(f"Mot de passe : {db_password}")

# Exemple fictif : utilisation de l'API_KEY
if api_key == "123456789abcdef":
    print("Clé API valide !")
else:
    print("Clé API invalide !")
