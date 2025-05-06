#!/bin/bash

set -e

echo "🔄 Convirtiendo notebooks a scripts..."
jupyter nbconvert --to script app/*.ipynb

echo "🧹 Eliminando líneas incompatibles con ejecución fuera de Jupyter..."
# Elimina cualquier uso de get_ipython(), sea de línea mágica o comando del sistema
find app -name "*.py" -exec sed -i '/get_ipython()/d' {} \;

echo "🚀 Buscando y ejecutando script principal..."
MAIN_SCRIPT=$(find app -name "*main.py" | head -n 1)

if [ -z "$MAIN_SCRIPT" ]; then
  echo "❌ No se encontró ningún archivo con 'main' en el nombre para ejecutar."
  exit 1
fi

echo "✅ Ejecutando $MAIN_SCRIPT"
python "$MAIN_SCRIPT"
