release: python manage.py migrate
web: daphne generator.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: celery -A generator.celery worker -l INFO
beat: celery -A generator beat wait -n