### main-ftm.py

#!/usr/bin/env python
# coding: utf-8




#----------------------------------
# ### Importación de librerias
#----------------------------------

import library_tfm_v0

from library_tfm_v0 import *

from dotenv import load_dotenv
import os


# Carga de CSV
import pandas as pd

# Funciones de carga de ficheros
import os

# Para generar el gráfico de dependecias
import networkx as nx
import matplotlib.pyplot as plt

# Calculo de localizaciones
import geocoder


#----------------------------------
# ### Importación de librerias
#----------------------------------





#----------------------------------
# ### Inicialización de Variables
#----------------------------------



########################################################################################################
# tabla de correspondencia
# Se detecta que los nombres de las columnas no coinciden entre las M4 y las GTFS

convert_list ={'idflinea':'route_id','idfestacion':'station_id','idestacion':'station_id','idanden':'platform_id'}

convert_keys =[]
convert_keys = [{'trip_id' : ['service_id', '0:5']},{'trip_id' : ['route_id', '5:9']}]

########################################################################################################


########################################################################################################
# variables para rutas y tipos de fichero a procesar
# file_paths = "C:\\Users\\MX0046001DC5030\\Downloads\\google_transit_M4" # Reemplaza con la ruta correcta

load_dotenv(dotenv_path='../.env')


# load_dotenv(dotenv_path='/.env') # por defecto lo espera en su directorio cosa que no es correcta
load_dotenv()

file_paths = os.getenv("PYTHON_FILE") #lo coge del env
# print ('file_paths :',file_paths)
extension= [".txt", ".csv"] # Lista de extensiones válidas a procesar
explore = 15 ## Parametro para delimitar el numero de elementos devueltos
########################################################################################################


split_key = 'df_M4' ## Raiz para la división entre dataframe 



#----------------------------------
# ### Inicialización de Variables
#----------------------------------



# # MAIN


limpiar_archivos(file_paths, extensiones=extension)


# Caga de los datos
dataframes = load_files_in_dataframes(file_paths, sep=',') # Asumiendo que el separador es la ,
'''
if dataframes:
    for fileName, df in dataframes.items():
        print(f"\nInformación del DataFrame '{f'df_{fileName}'}':") # Imprime el nombre del DataFrame
        
        print(f'Columnas :{globals()[f"df_{fileName}"].columns.tolist()}')


       #  print(f'CATA DEL DATAFRAME \n{globals()[f"df_{fileName}"].head(explore)}')
'''

####-------------------
# Propección de los df
####-------------------

for fileName, df in dataframes.items():
        print(f"\nInformación del DataFrame '{f'df_{fileName}'}':") # Imprime el nombre del DataFrame
        
        # print(f'Columnas :{globals()[f"df_{fileName}"].columns.tolist()}') #Imprime el nombre de cada columna 


        # print(f'CATA DEL DATAFRAME \n{globals()[f"df_{fileName}"].head(explore)}') #Imprime  un head de la tabla


# ## Identificar dependencias entre los Df



tempGlobal = globals() ## Para evitar que intervengan las variables de esta celda
relaciones = {}  # Define el diccionario relaciones aquí
relaciones_M4 = {}
relaciones_NO_M4 = {}

# Crear un grafo dirigido
G = nx.DiGraph()
G_NO_M4 = nx.DiGraph()
G_M4 = nx.DiGraph()
###PARA las tablas M4 y No M4 diferencias por la raiz

dependency_dataframes(globals())
tree_dataframes(globals())


# ## Pasos
# ### Cargar los datos 
# ### Función para identicar la boca de metro más cercana dada la localización del que pregunta 
# ### Función para identificar la geolocalización de la persona ✅ 
# 
# 



location_gps();
