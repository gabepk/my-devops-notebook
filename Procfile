release: python manage.py makemigrations & python manage.py migrate --settings=website.settings
web: gunicorn mysite.wsgi --log-file -
