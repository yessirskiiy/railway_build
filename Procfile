web: gunicorn generator:wsgi --log-file -
worker: celery -A generator worker --loglevel=info
beat: celery -A generator beat