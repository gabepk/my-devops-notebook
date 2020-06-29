release: python manage.py makemigrations & python manage.py migrate --settings=mysite.settings --run-syncdb
web: gunicorn mysite.wsgi --log-file -
