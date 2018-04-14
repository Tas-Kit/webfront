pylint --load-plugins pylint_django webfront

coverage run manage.py test -v 2
coverage html