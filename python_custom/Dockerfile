# Usamos una imagen base de Python 3.11
FROM python:3.11-slim

# Definir el directorio de trabajo dentro del contenedor
WORKDIR /app


# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt ./ 
# Copiar el archivo requirements.txt al contenedor
COPY .env ./ 

# Instalar las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente de la aplicación al contenedor
COPY . .

# Exponer el puerto 8000 para que sea accesible desde el exterior
EXPOSE 8000

# Comando para ejecutar la aplicación con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
