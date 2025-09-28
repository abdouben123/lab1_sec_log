import os
import base64
import subprocess
import requests


DB_PASSWORD = "admin123"


def run_command(command):
    return subprocess.check_output(command, shell=True)  # Risque d'injection


def get_api_key():
    return base64.b64decode("c2VjcmV0X2tleQ==").decode()  # Clé codée en base64


def fetch_data(url):
    response = requests.get(url, verify=False)  # Désactive la vérification SSL
    return response.text


import hashlib
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # MD5 est considéré faible


def read_file(filename):
    with open(f"/tmp/{filename}", "r") as f:  # Risque de path traversal
        return f.read()

if __name__ == "__main__":
    print("Code vulnérable pour test SonarQube")
