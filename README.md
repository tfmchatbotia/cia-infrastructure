

## Cómo usar

1. Clona el repositorio.
2. Crea un archivo `.env` basado en el ejemplo.

POSTGRES_USER=admin ## Usuario de la bases de datos

POSTGRES_PASSWORD=secretpassword ## Clave del usuario

POSTGRES_DB=mydb ## nombre del esquema

POSTGRES_HOST=tfm_ai_postgres_container ##nombre del contenedor que contiene la base de datos

PYTHON_FILE =../files ## Ruta donde se encuentran los ficheros a procesar

NOTA las variables el python las pone en minusculas para evitar posibles errores el codigo lo normaliza


3. Crea una replica del mismo en python_custom

4. Ejecuta:


```bash
docker-compose up -d



Creado un directorio python_custom

Aquí están las configuraciones de python

Dockerfile Crea un entorno python 3.11 y crean un entorno y añade nuestros requisitos de librerías y ejecuta la aplicación de carga quedando la instacia corriendo a pesar de que se halla ejecutado el codigo
Requirement.txt tiene las lista de librerías y versiones necesarias.

Creado un directorio app

Donde se encuentra el código consta de:

cia_data_loader_main.py (programa principal)

cia_data_loader_library.py librerías generadas para el proyecto

Veréis que hay un fichero __init__.py es el que permite que se pueda llamar a otros py sin errores 



el código de la api se llama a través de  127.0.0.1  

.- http://127.0.0.1:8000/docs documentación del servicio y se puede probar

 Tiene dos métodos un get y otro post es este último se puede ejecutar cualquier consulta sql 

En esta URL esta el Chat 

.- http://127.0.0.1:9000 Pagina del Chat con logos Ramon Areces y Universidad de Alcalá Simula la llamada esta el código comentado la  llamada real 


Sobre la base de datos

Dada esta configuración solo hay que comentar o des comentar la línea de la bbdd para que actualice los esquemas los esquemas + datos 

  
    volumes:
      - postgres_data:/var/lib/postgresql/data
      
      # - ./postgres_custom/estructure.sql:/docker-entrypoint-initdb.d/estructure.sql  # SOLO ESQUEMA
      
      - ./postgres_custom/estructure_full_data.sql:/docker-entrypoint-initdb.d/estructure_full_data.sql # ESQUEMA + DATOS



En caso de exportar la base de datos

borrar todo lo que venga por encima de 

COMMENT ON SCHEMA public IS 'standard public schema';

y poner el siguiente con tenido

--
-- PostgreSQL database dump
--

-- Dumped from database version 17.5 (Debian 17.5-1.pgdg120+1)
-- Dumped by pg_dump version 17.0

-- Started on 2025-05-13 12:29:32

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DO
$$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_database WHERE datname = 'mydb'
   ) THEN
      CREATE DATABASE mydb
         WITH TEMPLATE = template0
         ENCODING = 'UTF8'
         LOCALE_PROVIDER = libc
         LOCALE = 'en_US.utf8';
   END IF;
END
$$;


ALTER DATABASE mydb OWNER TO admin;

\connect mydb


SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA IF NOT EXISTS public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- TOC entry 3476 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

DO
$$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_database WHERE datname = 'mydb'
   ) THEN
      CREATE DATABASE mydb
         WITH TEMPLATE = template0
         ENCODING = 'UTF8'
         LOCALE_PROVIDER = libc
         LOCALE = 'en_US.utf8';
   END IF;
END
$$;


 

