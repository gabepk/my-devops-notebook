release: python manage.py makemigrations & python manage.py migrate --settings=mysite.settings & python manage.py collectstatic --clear & yes
web: gunicorn mysite.wsgi --log-file -
