#!/usr/bin/env python
# coding: utf-8

# # Funciones desarrolladas

# 1.2. 🛠️ Instalación

# ### 🔧Carga de librerias en el entorno

# In[1]:


# Carga de CSV
import pandas as pd

# Funciones de carga de ficheros
import os
# Para generar el gráfico de dependecias
import networkx as nx
import matplotlib.pyplot as plt
# Calculo de localizaciones
import math
import geocoder

import inspect


import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

import re
from collections import defaultdict
from collections import deque


from sqlalchemy import create_engine, inspect
import pandas as pd

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

from sqlalchemy.exc import SQLAlchemyError


# ## 💻 Funciones sobre el sistema

# ### clean_file
# 
# 🔍 ¿Qué hace?
# 
# Esta función recorre todos los archivos dentro de un **directorio (y sus subdirectorios)** y limpia los saltos de línea Windows (**\r\n**), reemplazándolos por saltos de línea estándar de Unix (\n), en archivos que tengan extensiones específicas (*por defecto, .txt*).
# 
# 🧱 ¿Qué hace paso a paso?
# 
# Recorrer el directorio y subdirectorios. 
# 
# La función filtra los archivos para solo procesar aquellos que tienen extensiones que coinciden con las proporcionadas en el parámetro extensions.
# 
# Abrir y leer el contenido del archivo:
# 
# Limpiar el contenido del archivo reemplaza los saltos de línea \r\n (utilizados en sistemas Windows) por \n (salto de línea estándar en sistemas Unix/Linux).
# 
# 
# Después de limpiar el contenido y se sobrescribe con el contenido limpio.
# 
# Manejo de errores:
# 
# Si ocurre un error durante la lectura o escritura del archivo, se captura con un bloque try-except y se imprime un mensaje de error, pero el proceso continúa con el siguiente archivo.
# 
# Si ocurre un error al recorrer los directorios o abrir el archivo principal, se devuelve un mensaje de error indicando la excepción.
# 

# In[2]:


def clean_file(directory, extensions=['.txt']):
    try : 
      for root, dirs, files in os.walk(directory):  # Recorrer directorios y subdirectorios
        for file_name in files:
            # print('extension:',extensions)
            if any(file_name.endswith(extension) for extension in extensions):  # Filtra por extensiones
                file_path = os.path.join(root, file_name)  # Obtiene la ruta completa
                # print(f'Procesando archivo: {file_path}')
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()

                    content_cleaned = content.replace('\r\n', '\n')

                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content_cleaned)

                    # print(f'✔ Procesado: {file_name}')

                except Exception as e:
                    print(f'❌ Error al procesar {file_name}: {e}. Se omitirá.')
    except Exception:
        return f'error {Exception}'
        
        


# In[3]:




# ## Importación de Librerias

# ## 📊 De tratamiento de las entidades del dataframe

# ### lowercase_if_letters_only
# 
# 🔍 ¿Qué hace?
# 
# Función para convertir a minúsculas solo las columnas con letras
# 
# 
# 🧱 ¿Qué hace paso a paso?
# 
#     1. Recorre todas las columnas del DataFrame.
#     2. Para cada columna:
#        - Convierte cada valor a cadena.
#        - Verifica si contiene solo letras. (para evitar tocar las columnas que tienen numeros
#     3. Si todos los valores de la columna son letras:
#        - Convierte la columna completa a minúsculas usando.
#     4. Devuelve el DataFrame modificado.

# In[4]:


def lowercase_if_letters_only(df_temp):
    try: 	
        for col in df_temp.columns:
            if df_temp[col].apply(lambda x: str(x).isalpha()).all():
                df_temp[col] = df_temp[col].str.lower()
        return df_temp
    except Exception:
        return f'error {Exception}'


# ### is_words(column)
# 
#  🔍 ¿Qué hace?
# 
#  Verifica si todos los valores de una columna son solo letras (sin números ni caracteres especiales)

# In[5]:


def is_words(column):
   return column.apply(lambda x: bool(re.match(r'^[A-Za-z]+$', str(x)))).all()


# ### lower_column
# 
# 🔍 ¿Qué hace?
# 
# Verifica si todos los valores en una serie contienen solo letras (ignorando strings vacíos).
# 

# In[6]:


def lower_column(df_temp, columns_str):
    for column in columns_str:
        if column in df_temp.columns:
            # Convertir la columna a tipo string, manejando nulos
            df_temp[column] = df_temp[column].fillna('').astype(str)
            
            # Verificar si todos los valores son letras
            if is_words(df_temp[column]):
                # Si todos los valores son letras, convertir a minúsculas
                df_temp[column] = df_temp[column].str.lower()

    return df_temp


# ### load_files_in_dataframes
# 
# 🔍 ¿Qué hace?
# 
# La función load_files_in_dataframes carga todos los archivos .csv o .txt de un directorio (y sus subdirectorios) en DataFrames de pandas, realizando varias transformaciones específicas.
# 
# 🧱 Paso a paso
# * Inicializa listas y diccionarios:
# 
# lista_id: almacena nombres de columnas que terminan en _id o empiezan por id.
# 
# dataframes: contiene los DataFrames con claves basadas en el nombre del archivo.
# 
# 🔹  Recorre los archivos del directorio:
# 
# * Ignora subdirectorios (aunque los recorre recursivamente).
# 
# 🔹 Filtra archivos por extensión (.csv o .txt).
# 
# * Procesa cada archivo válido:
# 
# * Lee el archivo como DataFrame con pandas.read_csv().
# 
# * Convierte los nombres de columnas a minúsculas.
# 
# * Renombra columnas usando convert_list.
# 
# * Realiza slicing o manipulación de columnas definidas en convert_keys.
# 
# * Si existe la columna objectid, la usa como índice.
# 
# 🔹 Limpieza de datos:
# 
# * Detecta columnas que contengan solo letras (excepto las columnas con id) y las convierte a minúsculas con lower_column.
# 
# 🔹 Guarda el resultado:
# 
# * Crea un DataFrame con nombre df_nombre_del_archivo.
# 
# * También lo guarda en el diccionario dataframes.
# 
# 🔹 Manejo de errores:
# 
# * Ignora archivos vacíos o con errores de análisis (pandas.errors.EmptyDataError o ParserError).
# 
# * Captura otros errores inesperados sin interrumpir el procesamiento.
# 
# 
# 

# In[7]:


def load_files_in_dataframes(file_path, sep=',', extensions=['.txt', '.csv']):
    all_ids = set()
    dataframes = {}

    try:
        for full_file_name in os.listdir(file_path):
            filepath = os.path.join(file_path, full_file_name)
            
            # Si es una subcarpeta, recursivamente procesa
            if os.path.isdir(filepath):
                sub_dataframes, sub_ids = load_files_in_dataframes(filepath, sep=sep, extensions=extensions)
                dataframes.update(sub_dataframes)
                all_ids.update(sub_ids)
                continue

            # Procesar solo archivos con extensión válida
            if any(full_file_name.endswith(ext) for ext in extensions):
                file_name = os.path.splitext(full_file_name)[0]  # sin extensión
                print(f'Procesando archivo: {full_file_name}')
                try:
                    df = pd.read_csv(filepath, sep=sep, header=0)
                    df.columns = df.columns.str.lower()  # Normalizar nombres de columnas
                    
                    # Detectar columnas ID
                    ids_in_file = [col for col in df.columns if col.endswith('_id') or col.startswith('id')]
                    all_ids.update(ids_in_file)
                    
                    if ids_in_file:
                        print(f'df_{file_name} contiene IDs: {ids_in_file}')

                    df_name = f"df_{file_name}"
                    globals()[df_name] = df  # no recomendable fuera de notebooks, pero útil en exploración
                    dataframes[file_name] = df

                except pd.errors.EmptyDataError:
                    print(f"Advertencia: El archivo {full_file_name} está vacío. Se omitirá.")
                except pd.errors.ParserError as e:
                    print(f"Error al analizar el archivo {full_file_name}: {e}. Se omitirá.")
                except Exception as e:
                    print(f"Error inesperado al procesar {full_file_name}: {e}. Se omitirá.")

        return dataframes, list(all_ids)

    except FileNotFoundError:
        print(f"Error: El directorio '{file_path}' no existe.")
        return {}, []
    except Exception as e:
        print(f"Error inesperado: {e}")
        return {}, []




# ### detect_keys
# 
# 🔍 ¿Que hace?
# 
# 🔹 Detectar automáticamente claves primarias y claves foráneas en un DataFrame de pandas, basándose en los nombres de columnas y si sus valores son únicos o repetidos.

# In[8]:


def detect_keys(df):
    # Detectar claves primarias (columnas únicas que terminan con '_id' o comienzan con 'id')
    primary_keys = [col for col in df.columns if df[col].is_unique and (col.endswith('_id') or col.startswith('id'))]
    
    # Detectar claves foráneas (columnas no únicas que terminan con '_id')
    foreign_keys = [col for col in df.columns if not df[col].is_unique and col.endswith('_id')]
    
    return primary_keys, foreign_keys 


# ### build_dependency_graph
# 
# 🔍 ¿Que hace?
# 
# La función construye un grafo de dependencias, entre tablas a partir de un conjunto de DataFrames de pandas. Este grafo permite conocer en qué orden se deben insertar las tablas en una base de datos relacional (como PostgreSQL), respetando sus dependencias por claves foráneas.

# In[9]:


def build_dependency_graph(dataframes):
    graph = defaultdict(list)  # Diccionario para almacenar las dependencias
    all_tables = set(dataframes.keys())  # Conjunto de todos los nombres de tablas

    for table_name, df in dataframes.items():
        # Detecta claves primarias y foráneas en el DataFrame
        _, foreign_keys = detect_keys(df)
        
        for fk in foreign_keys:
            # Elimina el sufijo '_id' para obtener el nombre de la tabla referenciada
            ref_table = fk[:-3] if fk.endswith('_id') else fk
            
            # Si la tabla referenciada existe en el conjunto de tablas, agrega la dependencia
            if ref_table in dataframes:
                graph[ref_table].append(table_name)
        
        # Asegura que la tabla actual esté en el grafo, incluso si no tiene dependencias
        if table_name not in graph:
            graph[table_name] = []

    return graph


# ### topological_sort_all_nodes
# 
# 🔍 ¿Que hace?
# 
# Su objetivo es determinar un orden de inserción de tablas en una base de datos respetando las dependencias entre ellas (por ejemplo, claves foráneas).

# In[10]:


def topological_sort_all_nodes(graph):
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    queue = deque([node for node in graph if indegree[node] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(graph):
        print("⚠️ Cuidado: se detectó una posible dependencia cíclica.")
    return order


# In[11]:


def topological_sort(graph):
    visited = set()
    order = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs(neighbor)
        order.append(node)

    for node in graph:
        dfs(node)

    return list(reversed(order))


# In[12]:


def get_unique_columns(df):
    """
    Retorna un diccionario con el nombre de la variable del DataFrame y sus columnas con valores únicos.
    """
    # Inspeccionar el stack para encontrar el nombre de la variable pasada como argumento
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    df_name = next((name for name, val in callers_local_vars if val is df), "dataframe")

    unique_cols = [col for col in df.columns if df[col].is_unique]
    return df_name,unique_cols




# ### insert_dataframes_to_postgres
# 
# 
# 🔍 ¿Qué hace?
# Inserta DataFrames en una base de datos PostgreSQL en el orden especificado, creando las tablas si no existen.
# 
#     Parámetros:
#         - dataframes: dict de DataFrames a insertar.
#         - insertion_order: orden de inserción (respetando claves foráneas).
#         - postgres_user: usuario de la base de datos.
#         - postgres_password: contraseña.
#         - postgres_db: nombre de la base de datos.
#         - host: dirección del servidor PostgreSQL.
#         - port: puerto del servidor.
#         - if_exists: comportamiento si la tabla existe ('fail', 'replace', 'append').
#         - unique_columns: Un diccionario que mapea el nombre de la tabla con las columnas que se deben considerar únicas para evitar duplicados. Esto es útil cuando queremos evitar que se inserten registros con valores duplicados en esas columnas.
# 
# 
# 
# 
# 🧱 Paso a paso
# 
# Conexión a la base de datos:
# 
# La función construye una URL de conexión a la base de datos usando las credenciales proporcionadas y establece una conexión utilizando SQLAlchemy (create_engine).
# 
# También se usa el inspector de SQLAlchemy para obtener información sobre las tablas existentes en la base de datos.
# 
# Recorrer las tablas en el orden de inserción:
# 
# La función recorre la lista insertion_order para insertar las tablas en el orden especificado.
# 
# Verificación de la existencia de tablas:
# 
# Si la tabla ya existe en la base de datos, la función imprime un mensaje indicando que la tabla existe.
# 
# Si la tabla no existe, se imprimirá un mensaje indicando que la tabla se creará automáticamente.
# 
# Eliminación de duplicados (si se especifica unique_columns):
# 
# Si se pasa el parámetro unique_columns, la función elimina las filas duplicadas de cada DataFrame basándose en las columnas definidas como "únicas" en unique_columns.
# 
# Este paso es importante porque solo se insertarán registros nuevos, evitando duplicados en la base de datos.
# 
# Inserción de los registros:
# 
# La función recorre cada fila del DataFrame y genera una consulta INSERT INTO utilizando la cláusula ON CONFLICT DO NOTHING.
# 
# Esto asegura que si ya existe un registro con las mismas columnas únicas (unique_cols), el registro no se inserte nuevamente (evita duplicados).
# 
# La consulta ON CONFLICT ({', '.join(unique_cols)}) DO NOTHING indica que, si ocurre un conflicto de clave (es decir, ya existe un registro con los mismos valores en las columnas indicadas en unique_cols), no se realiza ninguna acción (se ignora esa inserción).
# 
# Manejo de errores:
# 
# Si ocurre un error durante la inserción de algún registro (por ejemplo, un error SQL), la función captura la excepción y muestra el mensaje de error correspondiente.
# 

# ### insert_dataframes_to_postgres
# 
# 🔍 ¿Qué hace?
# 
#  Tiene como objetivo insertar datos de DataFrames de pandas en una base de datos PostgreSQL, evitando que se inserten registros duplicados basados en columnas únicas.

# In[13]:


def insert_dataframes_to_postgres(dataframes, insertion_order, postgres_user, postgres_password, postgres_db, host='localhost', port=5432, if_exists='replace', unique_columns=None):
    db_url = f"postgresql+psycopg2://{postgres_user}:{postgres_password}@{host}:{port}/{postgres_db}"
    print("db_url", db_url)
    engine = create_engine(db_url)
    
    for table in insertion_order:
        df = dataframes.get(table)
        if df is None:
            print(f"⚠️  No se encontró DataFrame para la tabla: {table}")
            continue
        print(f"🔄 Insertando en tabla: {table}")
        
        try:
            if unique_columns and table in unique_columns:
                unique_cols = unique_columns[table]
                df = df.drop_duplicates(subset=unique_cols, keep='first')
                print(f"🔍 Se eliminaron duplicados basados en las columnas: {unique_cols}")
            
            # Usar to_sql para insertar el DataFrame
            df.to_sql(table, engine, index=False, if_exists=if_exists)
            print(f"✅ Datos insertados correctamente en la tabla '{table}'")
        except SQLAlchemyError as e:
            print(f"❌ Error al insertar '{table}': {e}")
        except Exception as e:
            print(f"❌ Error inesperado al insertar '{table}': {e}")


# ## Dibujar graficos

# ### draw_graf
# 
# 🔍 ¿Qué hace?
# 
# Es una función para visualizar un grafo utilizando NetworkX para la estructura del grafo y Matplotlib para la visualización. 
# 
# 🧱 Explicación paso a paso
# 
# Los nodos están posicionados de manera automática utilizando el algoritmo de disposición de primavera.
# 
# Los nodos tienen un tamaño y color definidos.
# 
# Las etiquetas de los nodos muestran un atributo personalizado ('columnas_comunes').
# 
# Las aristas son flechas (porque el grafo es dirigido).
# 
# El grafo tiene un título que es pasado como parámetro.
# 
# Es ideal para representar estructuras de datos, redes de relaciones o dependencias entre elementos (como en análisis de grafos de dependencias o redes de información).

# In[14]:


def draw_graf(grafo, titulo, color):
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(grafo, k=2)
    nx.draw(grafo, pos, with_labels=True, node_size=5000, node_color=color, font_size=10, font_weight='bold', arrows=True)
    labels = nx.get_node_attributes(grafo, 'columnas_comunes')
    nx.draw_networkx_labels(grafo, pos, labels=labels, font_size=8, font_color='black')
    plt.title(titulo)
    plt.show()



# ### dependency_dataframes
# 
# 🔍 ¿Qué hace?
# 
# Analiza los DataFrames, crea grafos de dependencias y los visualiza.
# 
#     Args:
#     
#  🔹 globals_dict: Diccionario con variables globales (como globals()).
#  
#  🔹 split_key: Subcadena para separar DataFrames en dos grupos.
# 
# 🧱 Explicación paso a paso
# 
# 🔹 Clasifica las relaciones según si uno de los DataFrames contiene un prefijo como "df_M4".
# 
# 🔹 Dibuja un grafo visual para mostrar cómo están conectados.
# 
# 🔹 Devuelve toda esa información para poder usarla luego.
# 

# In[15]:


def dependency_dataframes(globals_dict, split_key="df_M4"):
    

    relaciones = {}
    relaciones_M4 = {}
    relaciones_NO_M4 = {}

    G = nx.DiGraph()
    G_NO_M4 = nx.DiGraph()
    G_M4 = nx.DiGraph()

    df_names = [name for name in globals_dict if name.startswith('df_') and isinstance(globals_dict.get(name), pd.DataFrame)]

    if not df_names:
        return {}, {}, {}, G, G_M4, G_NO_M4

    for dfx_name in df_names:
        try:
            df1 = globals_dict[dfx_name]
            columnas_df1 = list(df1.columns)

            for df2_name in df_names:
                if df2_name != dfx_name:
                    df2 = globals_dict[df2_name]
                    columnas_df2 = list(df2.columns)
                    columnas_comunes = list(set(columnas_df1) & set(columnas_df2))

                    if columnas_comunes:
                        if df2_name.startswith(split_key) or dfx_name.startswith(split_key):
                            relaciones_M4[f"{dfx_name} - {df2_name}"] = columnas_comunes
                            G_M4.add_edge(dfx_name, df2_name)
                        else:
                            relaciones_NO_M4[f"{dfx_name} - {df2_name}"] = columnas_comunes
                            G_NO_M4.add_edge(dfx_name, df2_name)

                        G.add_edge(dfx_name, df2_name)
                        relaciones[f"{dfx_name} - {df2_name}"] = columnas_comunes
        except KeyError as e:
            print(f"Error al acceder al DataFrame '{e}': Verifica que el DataFrame esté definido.")
            continue

    # Dibujar grafos
    plt.figure(figsize=(15, 10))
    pos = nx.spring_layout(G, k=0.8)

    nx.draw(G_M4, pos, with_labels=True, node_size=4000, node_color='lightblue',
            font_size=10, font_weight='bold', edge_color='blue', arrows=True)
    nx.draw(G_NO_M4, pos, with_labels=True, node_size=4000, node_color='green',
            font_size=10, font_weight='bold', edge_color='lightgreen', arrows=True)

    plt.title("Grafo de Dependencias entre DataFrames")
    plt.show()

    # Devolver resultados
    return relaciones, relaciones_M4, relaciones_NO_M4, G, G_M4, G_NO_M4



# ### tree_dataframes
# 
# 🔍 ¿Qué hace?
# 
# Analiza los DataFrames, crea un gráfico de arborescencia de dependencias y lo visualiza.
# 
# Args:
# 
# 🔹globals_dict: Diccionario con variables globales (como globals()).
#         
# 🔹split_key: Subcadena para separar DataFrames en dos grupos.
# 
# 🧱 ¿Qué hace paso a paso?
# 

# ## Funciones GPS
# 
# Aqui agrupamos las funciones de apoyo para temas de localización

# In[16]:


def tree_dataframes(globals_dict, split_key="df_M4"):
    relaciones = {}
    G = nx.DiGraph()

    # Detectar los DataFrames
    df_names = [
        name for name in globals_dict
        if name.startswith('df_') and isinstance(globals_dict[name], pd.DataFrame)
    ]

    if not df_names:
        print("No se encontraron DataFrames.")
        return

    # Buscar relaciones reales basadas en columnas comunes
    for dfx_name in df_names:
        df1 = globals_dict[dfx_name]
        columnas_df1 = set(df1.columns)

        for df2_name in df_names:
            if df2_name != dfx_name:
                df2 = globals_dict[df2_name]
                columnas_df2 = set(df2.columns)
                columnas_comunes = columnas_df1 & columnas_df2

                if columnas_comunes:
                    G.add_edge(dfx_name, df2_name)
                    relaciones[f"{dfx_name} -> {df2_name}"] = list(columnas_comunes)

    # Eliminar ciclos detectados para evitar dependencias circulares
    try:
        ciclo = list(nx.simple_cycles(G))
        if ciclo:
            print(f"Ciclos detectados en el grafo: {ciclo}")
            G.remove_edges_from([(n1, n2) for n1, n2 in G.edges() if (n1, n2) in ciclo])
    except nx.NetworkXError as e:
        print(f"Error al eliminar ciclos: {e}")
    
    # Encontrar nodos raíz (sin predecesores)
    posibles_raices = [n for n in G.nodes if G.in_degree(n) == 0]

    if not posibles_raices:
        print("No se encontró un DataFrame raíz. El grafo tiene ciclos o todos tienen predecesores.")
        return

    # Si hay más de una raíz, tratamos de crear árboles por separado para cada una
    arborescencias = {}
    for root_df in posibles_raices:
        try:
            T = nx.bfs_tree(G, root_df)
            arborescencias[root_df] = T
        except nx.NetworkXError as e:
            print(f"Error al construir el árbol desde {root_df}: {e}")
            continue

    # Mostrar relaciones
    for rel, cols in relaciones.items():
        print(f"{rel}: columnas comunes -> {cols}")

    # Dibujar todas las arborescencias encontradas
    plt.figure(figsize=(15, 10))
    pos = nx.spring_layout(G, k=0.8)

    # Dibujar cada árbol raíz
    for root_df, T in arborescencias.items():
        nx.draw(T, pos, with_labels=True, node_size=4000, node_color='lightblue',
                font_size=10, font_weight='bold', edge_color='blue', arrows=True)
    
    plt.title("Arborescencia de Dependencias entre DataFrames")
    plt.show()



# ### haversine
# 🔍 ¿Qué hace?
# 
# Calcula la distancia entre dos puntos en la superficie de la Tierra utilizando la fórmula de Haversine, que considera la curvatura del planeta (es decir, no asume una superficie plana como lo haría una distancia euclidiana).
# 
# Parámetros:
# 
#     🔹lat1, lon1: Latitud y longitud del primer punto (en grados decimales).
# 
#     🔹lat2, lon2: Latitud y longitud del segundo punto (también en grados decimales).
# 
# 🧠 Explicación paso a paso:
# 
#     🔹 Radio de la Tierra (R): Se toma como 6371 km (valor promedio).
# 
#     🔹 Conversión a radianes: Las funciones trigonométricas de math usan radianes, así que se convierte cada latitud y longitud de grados a radianes.
# 
#     🔹 Diferencia angular: Calcula la diferencia entre latitudes y longitudes en radianes (dlat, dlon).
# 
# 🎼 Fórmula de Haversine:
# 
#     🔹 Calcula el valor de a, que es una medida intermedia basada en el seno de las mitades de las diferencias angulares.
# 
#     🔹 Luego obtiene c, que es el ángulo central entre los dos puntos en una esfera.
# 
#     🔹 Distancia final: Multiplica el radio de la Tierra por c para obtener la distancia en kilómetros.

# In[17]:


def haversine(lat1, lon1, lat2, lon2):
    # Radio de la Tierra en kilómetros
    R = 6371.0
    
    # Convertir de grados a radianes
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    # Diferencias de latitudes y longitudes
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    # Fórmula de Haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Distancia en kilómetros
    distance = R * c
    return distance


# ### location_gps
# 🔍 ¿Qué hace?
# 
# Intenta determinar la ubicación del dispositivo basándose en la IP.
# 
# 🧠 ¿Qué hace paso a paso?
# 
# Llama a geocoder.ip('me'), que intenta determinar la ubicación del dispositivo basándose en la IP.
# 
# Extrae las coordenadas de latitud y longitud (latlng) del resultado.
# 
# Muestra las coordenadas por consola con print().

# In[18]:


def location_gps():
    ubicacion = geocoder.ip('me')
    
    # Mostrar coordenadas
    print(f"Tu ubicación aproximada es: {ubicacion.latlng}")

