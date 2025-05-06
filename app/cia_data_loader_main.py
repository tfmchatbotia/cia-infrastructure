#!/usr/bin/env python
# coding: utf-8

# # cia-data-loader

# ## Objetivos del sistema

# ✅ Leer cualquier fichero presente en el directorio file.
# 
# ✅ Generar los dataframe dinamicamente
# 
# ❌ Identificar las claves primarias de cada dataframe
# 
# ❌ Identificar las claves forneas de cada dataframe
# 
# ❌ Crear el esquema en Progress correspondiente a los ficheros incorporados.
# 
# ❌ Cargar los datos en esquema de base de datos
# 
# 

# ## 🛠️ Instalación

# En este epigrafe realizaremos todos los pasos necesarios para tener el entorno listo para la ejecución

# ###🔨.Requisitos Previos 

# ### get_environment_info 
# 
# Esta función detecta si el entorno donde se ejecuta el código es:
# 
# 🐳 Un contenedor Docker
# 
# 💻 Una máquina virtual (VM)
# 
# 🖥️ Un sistema físico (bare-metal)
# 
# **Dado que es necesario saber que tipo de entorno al principio es mas limpio crear esta función cargar las librerias**

# In[1]:


def get_environment_info():
    import os
    import platform
    import subprocess

    def is_docker():
        try:
            if os.path.exists("/.dockerenv"):
                return True
            with open("/proc/1/cgroup", "r") as f:
                if "docker" in f.read() or "containerd" in f.read():
                    return True
        except Exception:
            pass
        return False

    def is_virtual_machine():
        system = platform.system()

        try:
            if system == "Linux":
                try:
                    output = subprocess.check_output(["systemd-detect-virt"], stderr=subprocess.DEVNULL).decode().strip()
                    if output and output != "none":
                        return True, output
                except Exception:
                    pass

                try:
                    with open("/proc/cpuinfo", "r") as f:
                        if "hypervisor" in f.read().lower():
                            return True, "Desconocido (hypervisor detectado)"
                except Exception:
                    pass

                try:
                    output = subprocess.check_output(["dmidecode", "-s", "system-product-name"], stderr=subprocess.DEVNULL).decode().strip().lower()
                    for vm in ["virtualbox", "kvm", "vmware", "microsoft"]:
                        if vm in output:
                            return True, vm.capitalize()
                except Exception:
                    pass

            elif system == "Windows":
                try:
                    ps_script = "Get-CimInstance -ClassName Win32_ComputerSystem | Select-Object -ExpandProperty Model"
                    output = subprocess.check_output(["powershell", "-Command", ps_script], stderr=subprocess.DEVNULL).decode().strip().lower()
                    for vm in ["virtualbox", "kvm", "vmware", "hyper-v", "virtual"]:
                        if vm in output:
                            return True, vm.capitalize()
                except Exception:
                    pass

        except Exception:
            pass

        return False, None

    docker = is_docker()
    vm, vm_type = is_virtual_machine()

    if docker:
        entorno = "docker"
        is_virtual = True
    elif vm:
        entorno = "virtual"
        is_virtual = True
    else:
        entorno = "real"
        is_virtual = False

    return {
        "docker": docker,
        "virtual_machine": vm,
        "hypervisor": vm_type if vm else False,
        "entorno": entorno,
        "is_virtual" : is_virtual
    }



# Es necesario saber si el código esta corriendo en la maquina virtual o en local como paso previo ya que el ENV se ejecuta por parte de la máquina virtual en el arranque

# In[2]:




# ### ⛏️ Cadenas previas 

# In[3]:


env_info= get_environment_info()
# Al importar el codido py como notebook se genera esta linea que solo es necesario si se llama desde la máquina virtual

print (env_info)


# ### 🔧Carga de librerias en el entorno

# In[4]:


# Variables propias desarolladas por el equipo que ayuda a la construcción del TFM

import cia_data_loader_library
# Carga de todas las funciones generadas
from cia_data_loader_library import *

# Permite cargar configuraciones sensibles (como claves API, contraseñas, nombres de usuario, URLs) desde un archivo .env, sin tener que codificarlas directamente en tu script.
from dotenv import load_dotenv


# Carga de CSV
import pandas as pd


# Para generar el gráfico de dependecias
import networkx as nx
import matplotlib.pyplot as plt

# Calculo de localizaciones
import geocoder

# Permite cargar configuraciones sensibles (como claves API, contraseñas, nombres de usuario, URLs) desde un archivo .env, sin tener que codificarlas directamente en tu script.
from dotenv import dotenv_values

# Capacita para porder usar postgress SQL
from sqlalchemy import create_engine

from collections import deque


from collections import defaultdict


# ### 🔩 Carga de variables externas prefijadas

# In[5]:


# Cargar las variables del archivo .env en un diccionario al cargarlo al entorno para 

if (env_info.get("is_virtual") is True):
    env_vars = dotenv_values(".env")
else:
    env_vars = dotenv_values("cia-data-loader.env")
    
# Asignar cada variable como una variable Python, pero con nombre en minúsculas
# De esta forma no tengo que cargarlas manualmente 
for key, value in env_vars.items():
    globals()[key.lower()] = value 
    print(f'{key.lower()}={value}')


# ### 🔩Importación de librerias

# ## 💙 Main

# ### Inicialización de variables
# 
# En este punto daremos los valores a las variables 

# In[7]:


if env_info.get("is_virtual") is False:
    path_file = r'C:\Users\MX0046001DC5030\files'    
else:
    path_file = python_file
clean_file(path_file,extensions=['.txt', '.csv'])   
dataframes, list_id =load_files_in_dataframes(path_file, sep=',', extensions=['.txt', '.csv'])

# Identifica las dependecias
graph = build_dependency_graph(dataframes)

# order de carga de tablas
insertion_order = topological_sort_all_nodes(graph)
print ('env_info',env_info.get("is_virtual"))
if env_info.get("is_virtual") is False:
    host = 'localhost'
else :
    host = postgres_host
# inserta tablas
insert_dataframes_to_postgres(dataframes, insertion_order, postgres_user, postgres_password,postgres_db, host=host, port=5432, if_exists='replace')


# In[ ]:




