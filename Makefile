serve:
	python manage.py runserver

migration: # suffix with the name of app to make migrations for
	python manage.py makemigrations

migrate: # Apply migrations
	python manage.py migrate

test: # suffix with the app name tby which to run tests for
	python manage.py test

user: # create superuser
	python manage.py createsuperuser

static: # Collect Static
	python manage.py collectstatic