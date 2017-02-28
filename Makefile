
install:
	pip install -r requirements.txt
	python manage.py migrate

run:
	python manage.py runserver