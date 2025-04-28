#!/usr/bin/env python
# coding: utf-8

## Carga de ficheros En GTFS

# ## Pasos previos

#-------------------------
### Carga de Librerias
#-------------------------
# 


# Carga de CSV
import pandas as pd

# Fundiones de carga de ficheros
import os
# Para generar el gráfico de dependecias
import networkx as nx
import matplotlib.pyplot as plt
# Calculo de localizaciones
import math
import geocoder

'''
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
'''
##########################
# tabla de correspondencia
# Se detecta que los nombres de las columnas no coinciden entre las M4 y las GTFS
##########################

convert_list ={'idflinea':'route_id','idfestacion':'station_id','idestacion':'station_id','idanden':'platform_id'}


convert_keys = [
    {'trip_id' : ['service_id', '0:5']},
    {'trip_id' : ['route_id', '5:9']}
    
]

convert_keys = []


#----------------------------------
# ### Inicialización de Variables
#----------------------------------


extension= [".txt", ".csv"] # Lista de extensiones válidas a procesar
explore = 15 ## Parametro para delimitar el numero de elementos devueltos
split_key = 'df_M4' ## Raiz para la división entre dataframe 


# ### Funciones

# #### Cargar ficheros

import os

def limpiar_archivos(directorio, extensiones):
    """
    Reemplaza \r\n por \n en archivos con extensiones dadas.
    Guarda los archivos en UTF-8 y sobrescribe los originales.
    Recorre subdirectorios de forma recursiva.
    """
    for root, dirs, files in os.walk(directorio):  # Recorrer directorios y subdirectorios
        for nombre_archivo in files:
            # print('extensiones:',extensiones)
            if any(nombre_archivo.endswith(ext) for ext in extensiones):  # Filtra por extensiones
                ruta_archivo = os.path.join(root, nombre_archivo)  # Obtiene la ruta completa
                # print(f'Procesando archivo: {ruta_archivo}')
                
                try:
                    with open(ruta_archivo, 'r', encoding='utf-8', errors='ignore') as f:
                        contenido = f.read()

                    contenido_limpio = contenido.replace('\r\n', '\n')

                    with open(ruta_archivo, 'w', encoding='utf-8') as f:
                        f.write(contenido_limpio)

                    # print(f'✔ Procesado: {nombre_archivo}')

                except Exception as e:
                    print(f'❌ Error al procesar {nombre_archivo}: {e}. Se omitirá.')



def format_trip_id(row):
    route_id = row['route_id']
    line = row['idftramo']
    if pd.isnull(route_id):
        return None

    line = line.split(route_id)[1]
    return f"4_I{route_id}_2023I_{line}"

    try:
        # Quitamos el prefijo "4__" y separamos
        parts = route_id.replace('4__', '')  # ['12', '1', '', '']
        linea = parts[0]  # "12"
        if linea =='_':
            linea = parts[1] 
        print('linea',linea)
        sublinea = parts[1]  # "1"
        padded_sublinea = str(int(sublinea)).zfill(3)  # "001"

        return f"4_I{linea}-{padded_sublinea}_2023I_"

    except Exception:
        return f"4_I{route_id}_2023I_"






def load_files_in_dataframes(path_, sep=','):
    """
    Carga archivos .txt o .csv de un directorio en DataFrames de pandas,
    creando un DataFrame con el nombre 'df_' + nombre del archivo.

    Args:
        path_: La ruta al directorio que contiene los archivos .txt.
        sep: El separador de campos en los archivos (por defecto ',').
              Puede ser ',', '\t', ' ', etc.

    Returns:
        Un diccionario donde las claves son los nombres de los archivos (sin extensión)
        y los valores son los DataFrames correspondientes. Devuelve None si hay un error.
    """
    # print(f'Ruta: {path_}')
    lista_id =[]
    lista_id_=[]
    dataframes = {}
    try:
        # print(f'Ruta: {path_}')
        for fullfilename in os.listdir(path_):
            if any(fullfilename.endswith(ext) for ext in extension):
                filename_ = fullfilename[:-4]
                filepath = os.path.join(path_, fullfilename)
                print(f'Procesando archivo: {fullfilename}')
                try:
                    df = pd.read_csv(filepath, sep=sep, header=0)
                    ## 
                    df.columns = df.columns.str.lower()
                    # Normalizamos los nombres de las columnas
                    df.rename(columns={col: convert_list[col] for col in df.columns if col in convert_list}, inplace=True)
                    for mapping in convert_keys:
                        for source_col, (target_col, slice_str) in mapping.items():
                            if source_col in df.columns and target_col not in df.columns:
                              	start, end = map(int, slice_str.split(':'))
                                
                            if target_col == 'route_id':
                              	df[target_col] = df[source_col].str.split('-').str[1].str.split('_').str[0]
                              	df[target_col] = pd.to_numeric(df[target_col], errors='coerce')  # Convierte '' y errores a NaN
                              	df[target_col] = df[target_col].apply(lambda x: f"4__{int(x)}" if pd.notnull(x) else None)
                                                                                   
                            else:
                                df[target_col] = df[source_col].str[start:end]

                                
                    '''if 'idftramo' in df.columns:
                            df['tripp_id'] = df.apply(format_trip_id, axis=1)
'''
                    
                       
                    if 'objectid'in df.columns:
                        df.reset_index(drop=True, inplace=True)  # elimina el índice anterior por si venía de otro DataFrame
                        df.set_index('objectid', inplace=True)    
                    # Crea un DataFrame con el nombre 'df_' + nombre del archivo:
                    
                    lista_id_ =[col for col in df.columns if col.endswith('_id')]
                    
                    lista_id =[col for col in df.columns if col.startswith('id')]
                     
                    lista_id =lista_id +lista_id_
                    if len(lista_id):
                        print (f'df_{filename_} lista:{lista_id}')   
                        
                    
                    
                    df_name = f"df_{filename_}"  # Crea el nombre del DataFrame
                    globals()[df_name] = df  # Crea una variable global con el nuevo nombre
                    dataframes[filename_] = df
                except pd.errors.EmptyDataError:
                    print(f"Advertencia: El archivo {fullfilename} está vacío. Se omitirá.")
                except pd.errors.ParserError as e:
                    print(f"Error al analizar el archivo {fullfilename}: {e}. Verifica el separador y el formato del archivo. Se omitirá.")
                except Exception as e:
                    print(f"Error inesperado al procesar {fullfilename}: {e}. Se omitirá.")
        return dataframes
    except FileNotFoundError:
        print(f"Error: El directorio '{path_}' no existe.")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None


# #### Dibujar graficos

def draw_graf(grafo, titulo, color):
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(grafo, k=2)
    nx.draw(grafo, pos, with_labels=True, node_size=5000, node_color=color, font_size=10, font_weight='bold', arrows=True)
    labels = nx.get_node_attributes(grafo, 'columnas_comunes')
    nx.draw_networkx_labels(grafo, pos, labels=labels, font_size=8, font_color='black')
    plt.title(titulo)
    plt.show()


# #### Dibujar Analisis de dependecias entre Dataframes
# 



def dependency_dataframes(globals_dict, split_key="df_M4"):
    """
    Analiza los DataFrames, crea grafos de dependencias y los visualiza.

    Args:
        globals_dict: Diccionario con variables globales (como globals()).
        split_key: Subcadena para separar DataFrames en dos grupos.
    """
    relaciones = {}
    relaciones_M4 = {}
    relaciones_NO_M4 = {}

    G = nx.DiGraph()
    G_NO_M4 = nx.DiGraph()
    G_M4 = nx.DiGraph()

    df_names = [name for name in globals_dict if name.startswith('df_') and isinstance(globals_dict.get(name), pd.DataFrame)]

    if not df_names:
        print("No se encontraron DataFrames en globals().")
        return

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
            print(f"Error al acceder al DataFrame '{e}':  Verifica que el DataFrame esté definido.")
            continue  # Salta al siguiente DataFrame si hay un error


    # Mostrar relaciones (formato mejorado)
    '''for relacion, columnas in relaciones.items():
        print(f"Relación: {relacion}, Columnas comunes: {columnas}")
        print("-" * 20)
'''
    # Dibujar grafos (con color naranja para G_NO_M4)
    plt.figure(figsize=(15, 10))  # Figura más grande para mejor visualización

    pos = nx.spring_layout(G, k=0.8) # Ajustado k para mejor separación

    nx.draw(G_M4, pos, with_labels=True, node_size=4000, node_color='lightblue', font_size=10, font_weight='bold',  edge_color='blue',arrows=True)
   
    nx.draw(G_NO_M4, pos, with_labels=True, node_size=4000, node_color='green', font_size=10, font_weight='bold', edge_color='lightgreen', arrows=True)

    plt.title("Grafo de Dependencias entre DataFrames")
    plt.show()

# Ejemplo de uso (asegúrate de tener tus DataFrames definidos):
#dependency_dataframes(globals())





# ##### Arborescencia 





def tree_dataframes(globals_dict, split_key="df_M4"):
    """
    Analiza los DataFrames, crea un gráfico de arborescencia de dependencias y lo visualiza.

    Args:
        globals_dict: Diccionario con variables globales (como globals()).
        split_key: Subcadena para separar DataFrames en dos grupos.
    """
    relaciones = {}
    relaciones_M4 = {}
    relaciones_NO_M4 = {}

    G = nx.DiGraph()
    G_NO_M4 = nx.DiGraph()
    G_M4 = nx.DiGraph()

    df_names = [name for name in globals_dict if name.startswith('df_') and isinstance(globals_dict.get(name), pd.DataFrame)]

    if not df_names:
        print("No se encontraron DataFrames en globals().")
        return

    # Crear relaciones entre los DataFrames manualmente (esto es solo un ejemplo)
    for df_name in df_names:
        # Lógica para establecer dependencias entre DataFrames (esto es solo un ejemplo)
        # Si el DataFrame 'df_name' depende de otro (puedes usar alguna lógica de nombres)
        for other_df in df_names:
            if df_name != other_df:
                # Aquí debes definir cómo determinar que un DataFrame depende de otro.
                # Por ejemplo, si un DataFrame contiene el nombre de otro DataFrame en sus columnas.
                G.add_edge(df_name, other_df)

    # Encuentra el DataFrame raíz (sin dependencias)
    root_df = None
    for dfx_name in df_names:
        if all(dfx_name != df2_name for df2_name in df_names if (dfx_name, df2_name) in G.edges):
            root_df = dfx_name
            break

    if root_df is None:
        print("No se encontró un DataFrame raíz. No se puede crear la arborescencia.")
        return

    # Ordena los DataFrames por orden de dependencia
    sorted_df_names = [root_df]
    for dfx_name in df_names:
        if dfx_name != root_df:
            for df2_name in sorted_df_names:
                if (df2_name, dfx_name) in G.edges:
                    sorted_df_names.insert(sorted_df_names.index(df2_name) + 1, dfx_name)
                    break

    # Construye el gráfico de arborescencia
    try:
        T = nx.bfs_tree(G, root_df)
    except nx.NetworkXError as e:
        print(f"Error al construir el árbol: {e}")
        return

    # Mostrar relaciones (formato mejorado)
    for relacion, columnas in relaciones.items():
        print(f"Relación: {relacion}, Columnas comunes: {columnas}")
        print("-" * 20)

    # Dibujar el gráfico de arborescencia
    plt.figure(figsize=(15, 10))  # Figura más grande para mejor visualización
    pos = nx.spring_layout(T, k=0.8)  # Ajustado k para mejor separación

    nx.draw(T, pos, with_labels=True, node_size=4000, node_color='lightblue', font_size=10, font_weight='bold', edge_color='blue', arrows=True)
    
    plt.title("Arborescencia de Dependencias entre DataFrames")
    plt.show()

# Ejemplo de uso (asegúrate de tener tus DataFrames definidos):
# dependency_dataframes(globals())
tree_dataframes(globals())


# #### Calcular la distancias


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

# Ejemplo de uso
lat1, lon1 = 40.748817, -73.985428  # Coordenadas de ejemplo: New York (lat, lon)
lat2, lon2 = 34.052235, -118.243683  # Coordenadas de ejemplo: Los Angeles (lat, lon)

distancia = haversine(lat1, lon1, lat2, lon2)
print(f"La distancia entre las dos ubicaciones es: {distancia:.2f} km")


# ##### Obtener ubicación basada en IP



def location_gps():
    ubicacion = geocoder.ip('me')
    
    # Mostrar coordenadas
    print(f"Tu ubicación aproximada es: {ubicacion.latlng}")



