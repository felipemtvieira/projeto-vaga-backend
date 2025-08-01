#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

# Executa as migrações do banco de dados
python manage.py makemigrations
python manage.py migrate

# Executa o comando principal do container
exec "$@"