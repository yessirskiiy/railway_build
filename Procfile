release: python manage.py migrate
web: daphne generator.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: celery -A generator.celery worker & celery -A generator beat -l INFO & wait -n