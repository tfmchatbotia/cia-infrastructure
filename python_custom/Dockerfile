# Usa imagen base oficial de Python
FROM python:3.11-slim

# Establece directorio de trabajo en la imagen
WORKDIR /app

# Instala Supervisor
RUN apt-get update && apt-get install -y supervisor

# Copia todo lo necesario desde el contexto correcto
COPY ./templates /app/templates
COPY ./static /app/static
COPY ./main.py /app/
COPY ./web_main.py /app/
COPY ./supervisord.conf /app/
COPY ./requirements.txt /app/

# Instala dependencias de Python
RUN pip install --no-cache-dir -r /app/requirements.txt

# Comando por defecto
CMD ["supervisord", "-c", "/app/supervisord.conf"]

