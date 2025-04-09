# entrypoint.sh
#!/bin/sh

echo "🚀 Esperando o banco ficar pronto..."
sleep 10

echo "📦 Rodando migrações..."
python manage.py migrate --noinput

echo "🧹 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "🔥 Iniciando o Gunicorn..."
gunicorn personal_website.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 120
