release: python manage.py makemigrations & python manage.py migrate --settings=mysite.settings & yes | python manage.py collectstatic --clear
web: gunicorn mysite.wsgi --log-file -
