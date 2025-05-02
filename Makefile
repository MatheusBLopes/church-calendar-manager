PROJECT_NAME = $(shell pwd | rev | cut -f1 -d'/' - | rev)

runserver:
	poetry run python church-calendar-manager/manage.py runserver

migrate:
	poetry run python church-calendar-manager/manage.py migrate

makemigrations:
	poetry run python church-calendar-manager/manage.py makemigrations

lint:
	poetry run pre-commit run --all-files

run-gunicorn:
	gunicorn -c gunicorn_config.py quizhero_api.wsgi:application

test:
	poetry run pytest -sx $(PROJECT_NAME) --reuse-db --create-db

collect-static:
	poetry run python church-calendar-manager/manage.py collectstatic

createsuperuser:
	poetry run python church-calendar-manager/manage.py createsuperuser


# DOCKER
run-container:
	docker run -p 8000:8000 church-calendar-manager
