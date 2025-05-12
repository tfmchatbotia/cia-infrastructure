from fastapi import FastAPI, Request
import databases
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Convertir todas las variables de entorno a min�sculas
env_vars = {key.lower(): value for key, value in os.environ.items()}

# Obtener la URL de la base de datos utilizando las variables de entorno en min�sculas
DATABASE_URL = f"postgresql://{env_vars.get('postgres_user')}:{env_vars.get('postgres_password')}@{env_vars.get('postgres_host')}:{5432}/{env_vars.get('postgres_db')}"
print('DATABASE_URL', DATABASE_URL)

# Inicializar la base de datos con la URL generada
database = databases.Database(DATABASE_URL)

from fastapi import FastAPI
import asyncpg
import os
from dotenv import load_dotenv
# Permite cargar configuraciones sensibles (como claves API, contrase�as, nombres de usuario, URLs) desde un archivo .env, sin tener que codificarlas directamente en tu script.
from dotenv import dotenv_values


# Cargar variables del entorno desde .env

env_vars = dotenv_values(".env")

# Obtener todas las variables de entorno cargadas
# Asignar cada variable como una variable Python, pero con nombre en min�sculas
# De esta forma no tengo que cargarlas manualmente 
for key, value in env_vars.items():
    globals()[key.lower()] = value 
    print(f'{key.lower()}={value}')




    
# Construir la URL de conexi�n
db_url = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{5432}/{postgres_db}"
print (db_url)
app = FastAPI()

# Endpoint ra�z que hace SELECT 1
@app.get("/")
async def read_root():
    try:
        conn = await asyncpg.connect(db_url)
        result = await conn.fetch("SELECT 1")
        await conn.close()
        return {"message": "Database connection successful", "result": [dict(r) for r in result]}
    except Exception as e:
        return {"error": str(e)}