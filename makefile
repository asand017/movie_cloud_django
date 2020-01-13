build:
	python manage.py check
	python manage.py makemigrations
	python manage.py migrate
