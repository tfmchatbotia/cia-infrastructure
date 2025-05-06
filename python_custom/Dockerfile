FROM python:3.10-slim

RUN pip install --no-cache-dir jupyter nbconvert pandas sqlalchemy psycopg2-binary networkx python-dotenv matplotlib geocoder

# Copia el script de entrada
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

WORKDIR /app
COPY . /app

ENTRYPOINT ["/entrypoint.sh"]
