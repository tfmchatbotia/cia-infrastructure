# Usa la imagen oficial de PostgreSQL como base
FROM postgres:latest

# Establece las variables de entorno desde el archivo .env
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_DB=${POSTGRES_DB}

# Expone el puerto estándar de PostgreSQL
EXPOSE 5432
