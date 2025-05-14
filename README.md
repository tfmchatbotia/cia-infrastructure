
Dada esta configuración solo hay que comentar o descomentar la linea de la bbdd para que carge los esquemas los esquemas + datos 

  tfm_ai_postgres:
    image: postgres:16
    build:
      context: ./postgres_custom
    container_name: tfm_ai_postgres_container
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    ports:
      - "127.0.0.1:5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      # - ./postgres_custom/estructure.sql:/docker-entrypoint-initdb.d/estructure.sql  # SOLO ESQUEMA
      - ./postgres_custom/estructure_full_data.sql:/docker-entrypoint-initdb.d/estructure_full_data.sql # ESQUEMA + DATOS
    networks:
      - tfm_ai_network






## Cómo usar

1. Clona el repositorio.
2. Crea un archivo `.env` basado en el ejemplo.

POSTGRES_USER=admin ## Usuario de la bases de datos

POSTGRES_PASSWORD=secretpassword ## Clave del usuario

POSTGRES_DB=mydb ## nombre del esquema

POSTGRES_HOST=tfm_ai_postgres_container ##nombre del contenedor que contiene la base de datos

PYTHON_FILE =../files ## Ruta donde se encuentran los ficheros a procesar
3. Crea una replica del mismo en python_custom

4. Ejecuta:


```bash
docker-compose up -d


docker-compose que contiene el codigo python para la carga de ficheros

Creado un directorio python_custom

Aquí están las configuraciones de python

Dockerfile Crea un entorno python 3.11 y crean un entorno y añade nuestros requisitos de librerías y ejecuta la aplicación de carga quedando la instacia corriendo a pesar de que se halla ejecutado el codigo
Requirement.txt tiene las lista de librerías y versiones necesarias.
Creado un directorio app

Donde se encuentra el código consta de:

cia_data_loader_main.py (programa principal)
cia_data_loader_library.py librerías generadas para el proyecto
Veréis que hay un fichero __init__.py es el que permite que se pueda llamar a otros py sin errores 


el codigo de la api se llama a traves de  127.0.0.1  
.- http://127.0.0.1:8000/docs documentación del servicio y se puede probar


