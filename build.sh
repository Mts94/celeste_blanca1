#!/usr/bin/env bash
# Termina si hay algún error
set -o errexit  

echo "🚀 Instalando dependencias..."
pip install -r requirements.txt

echo "📦 Aplicando migraciones..."
python manage.py migrate --noinput

echo "🗂️ Recolectando static files..."
python manage.py collectstatic --noinput

echo "✅ Build finalizado correctamente."
