#!/usr/bin/env bash
set -o errexit  # termina si hay algún error

echo "Instalando dependencias..."
pip install -r requirements.txt

echo "Aplicando migraciones..."
python manage.py migrate --noinput

echo "Recolectando static files..."
python manage.py collectstatic --noinput
