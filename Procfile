release: python manage.py makemigrations & python manage.py migrate --settings=mysite.settings
web: gunicorn mysite.wsgi --log-file -
