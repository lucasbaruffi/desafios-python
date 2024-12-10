# Fazer o armazenamento seguro de informações
# Utilizar um arquivo .env = .gitignore para isso

# Coloquei isso no .env:
# APP_USER=admin
# APP_PASSWORD=@123AB

# Coloquei também uma "cópia" do .env no .env.example

import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("APP_USER")
password = os.getenv("APP_PASSWORD")

print(f"""Usuário: {user}
Senha: {password}""")