.PHONY: all

all: install migrations initial static test coverage run

coverage:
	coverage run --source='.' manage.py test blogger
	coverage report -m

coverage-html:
	coverage html

docb:
	cd docker && docker-compose up --build

docd:
	cd docker && docker-compose up -d --build

docdown:
	cd docker && docker-compose down -v

install:
	pip install -r requirements.txt

migrations:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver 127.0.0.1:8000

static:
	python manage.py collectstatic --noinput

test:
	python manage.py test blogger
