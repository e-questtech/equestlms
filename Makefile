branch_name = $$(git branch --show-current)
changed_files = $$(git ls-files '*.py')
os_type = $$(uname -sr)

checks: lint test

env:
	python -m venv env

update:
	pip install -r requirements.txt

activate:
	source venv/bin/activate

test:
	python manage.py test -v 2 --keepdb

lint:
	pylint $(changed_files)
	flake8 .

server:
	python manage.py runserver 0.0.0.0:8000

migrate:
	python manage.py makemigrations
	python manage.py migrate

push:
	git pull
	git push -u origin $(branch_name)
