from fastapi import FastAPI, Request
from pydantic import BaseModel
import asyncpg
import os
from dotenv import dotenv_values

# Cargar variables desde .env
env_vars = dotenv_values(".env")

# Asignar variables a globals
for key, value in env_vars.items():
    globals()[key.lower()] = value
    print(f'{key.lower()}={value}')

# URL de conexión
db_url = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{5432}/{postgres_db}"
print("db_url:", db_url)

app = FastAPI()

# Modelo para recibir SQL desde el cliente
class SQLQuery(BaseModel):
    query: str

@app.get("/")
async def read_root():
    try:
        conn = await asyncpg.connect(db_url)
        result = await conn.fetch("SELECT 1")
        await conn.close()
        return {"message": "Database connection successful", "result": [dict(r) for r in result]}
    except Exception as e:
        return {"error": str(e)}

@app.post("/execute-sql")
async def execute_sql(query_data: SQLQuery):
    try:
        conn = await asyncpg.connect(db_url)
        result = await conn.fetch(query_data.query)
        await conn.close()
        return {"success": True, "result": [dict(r) for r in result]}
    except Exception as e:
        return {"success": False, "error": str(e)}
