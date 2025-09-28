
import os
import hvac


VAULT_ADDR = os.getenv("VAULT_ADDR", "http://127.0.0.1:8200")
VAULT_TOKEN = os.getenv("VAULT_TOKEN")

if not VAULT_TOKEN:
    raise SystemExit("Erreur: VAULT_TOKEN non défini. export VAULT_TOKEN='ton_token_vault'")

client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)


secret = client.secrets.kv.v2.read_secret_version(path='myapp')
data = secret['data']['data']

db_user = data.get('db_user')
db_password = data.get('db_password')
api_key = data.get('api_key')

print("DB_USER:", db_user)
print("DB_PASSWORD:", db_password)
print("API_KEY:", api_key)
