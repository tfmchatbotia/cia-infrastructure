# Usa una imagen oficial de Python 3.11 ligera como imagen base
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Actualiza pip a la última versión
RUN pip install --upgrade pip

# Instala virtualenv para crear entornos virtuales
RUN pip install virtualenv

# Crea un entorno virtual en el contenedor
RUN python -m venv /venv

# Añade el entorno virtual al PATH para que sea el intérprete por defecto
ENV PATH="/venv/bin:$PATH"

# Copia el archivo de requerimientos al contenedor
COPY ./requirements.txt /python_custom/

# Instala las dependencias de la aplicación usando el entorno virtual
RUN pip install -r /python_custom/requirements.txt

# Copia el código fuente de tu aplicación al contenedor
COPY . /app/

# Comando por defecto para arrancar la aplicación FastAPI usando uvicorn
# Cambia "your_app_name" por el nombre de tu archivo sin .py, por ejemplo: "main"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

