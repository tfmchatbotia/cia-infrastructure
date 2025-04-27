# PostgreSQL Docker Setup

Este proyecto levanta un contenedor PostgreSQL con Docker usando `docker-compose`.
# Crea la base de datos vacia con las tablas
## Cómo usar

1. Clona el repositorio.
2. Crea un archivo `.env` basado en el ejemplo.



3. Ejecuta:


```bash
docker-compose up -d




docker-compose crea dos contenedores uno para la base de datos y otro para python 
.env fichero de configuración con las variables comunes a toda la plataforma 
Creado un directorio postgres_custom

esquema.sql modelo inicial de la base de datos
Dockerfile copia la base de datos al contenedor sino existe y activa la base de datos  
Creado un directorio python_custom 

Aquí están las configuraciones de python

Dockerfile Crea un entorno python 3.11 y crean un entorno y añade nuestros requisitos de librerías y ejecuta el programa de validación de conectividad de la base de datos
Requirement.txt tiene las lista de librerías y versiones necesarias.
Creado un directorio app

Donde se encuentra el código consta de:

main.py (programa principal)
Librería database_test.py llama a la base de datos de postgress los parámetros de configuración los coge del fichero de configuración .env
Veréis que hay un fichero __init__.py es el que permite que se pueda llamar a otros py sin errores 