release: python manage.py makemigrations & python manage.py migrate --settings=mysite.settings --run-syncdb & python manage.py migrate --settings=mysite.settings --fake
web: gunicorn mysite.wsgi --log-file -
