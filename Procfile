web: daphne generator.asgi:application --port $PORT --bind 0.0.0.0 -v2
celery: celery --app=generator worker -loglevel=info
celerybeat: celery -A generator beat