
## Cómo usar

1. Clona el repositorio.
2. Crea un archivo `.env` basado en el ejemplo.

POSTGRES_USER=admin ## Usuario de la bases de datos

POSTGRES_PASSWORD=secretpassword ## Clave del usuario

POSTGRES_DB=mydb ## nombre del esquema

POSTGRES_HOST=tfm_ai_postgres_container ##nombre del contenedor que contiene la base de datos

PYTHON_FILE =../files ## Ruta donde se encuentran los ficheros a procesar


3. Ejecuta:


```bash
docker-compose up -d




docker-compose que contiene el codigo python para la carga de ficheros

Creado un directorio python_custom

Aquí están las configuraciones de python

Dockerfile Crea un entorno python 3.11 y crean un entorno y añade nuestros requisitos de librerías y ejecuta la aplicación de carga quedando la instacia corriendo a pesar de que se halla ejecutado el codigo
Requirement.txt tiene las lista de librerías y versiones necesarias.
Creado un directorio app

Donde se encuentra el código consta de:

main_tfm.py (programa principal)
library_tfm_v0.py librerías generadas para el proyecto
Veréis que hay un fichero __init__.py es el que permite que se pueda llamar a otros py sin errores 