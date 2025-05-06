from fastapi import FastAPI
import asyncpg
import os
from dotenv import load_dotenv
# Permite cargar configuraciones sensibles (como claves API, contraseñas, nombres de usuario, URLs) desde un archivo .env, sin tener que codificarlas directamente en tu script.
from dotenv import dotenv_values


# Cargar variables del entorno desde .env

env_vars = dotenv_values(".env")

# Obtener todas las variables de entorno cargadas
# Asignar cada variable como una variable Python, pero con nombre en minúsculas
# De esta forma no tengo que cargarlas manualmente 
for key, value in env_vars.items():
    globals()[key.lower()] = value 
    print(f'{key.lower()}={value}')




    
# Construir la URL de conexión
db_url = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{5432}/{postgres_db}"
print (db_url)
app = FastAPI()

# Endpoint raíz que hace SELECT 1
@app.get("/")
async def read_root():
    try:
        conn = await asyncpg.connect(db_url)
        result = await conn.fetch("SELECT 1")
        await conn.close()
        return {"message": "Database connection successful", "result": [dict(r) for r in result]}
    except Exception as e:
        return {"error": str(e)}




