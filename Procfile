web: daphne generator.asgi:application
worker: celery -A generator worker --loglevel=info
beat: celery -A generator beat