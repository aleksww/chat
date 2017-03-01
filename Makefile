
db:
	sudo service postgresql start
	sudo service redis-server start
	

install:
	pip install -r requirements.txt
	python manage.py migrate

run:
	python manage.py runserver $(IP):$(PORT)