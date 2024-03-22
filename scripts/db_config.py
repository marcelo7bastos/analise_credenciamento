from dotenv import load_dotenv
import os

load_dotenv()  # Carrega variáveis de ambiente do arquivo .env

# Credenciais
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
