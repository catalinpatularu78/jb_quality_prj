#!/bin/sh

set -e #exit the script if there are any errors

python manage.py collectstatic --noinput

uwsgi --socket :8000 --master --enable-threads --module jb_quality.wsgi  #command that runs the application using the uwsgi service in the foreground