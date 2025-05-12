FROM python:3.11-slim

# Definir el directorio de trabajo
WORKDIR /app

# Copiar primero requirements y .env antes del resto del código
COPY requirements.txt ./
COPY .env .env

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

EXPOSE 8000

# Ejecutar la app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
