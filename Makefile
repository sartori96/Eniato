activate:
	python -m venv eniato; \
	source eniato/Scripts/activate; \

install:
	pip install -e .['dev']

run:
	export FLASK_ENV=development && \
	export FLASK_APP=dependencias/app.py && \
	flask run

all: activate install run