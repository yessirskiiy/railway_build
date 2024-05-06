web: daphne generator.asgi:application --port $PORT --bind 0.0.0.0 -v2
celery: python -m celery -A generator worker -l info
celerybeat: celery -A generator beat