activate:
	source enitato/Scripts/activate

install:
	pip install -e .['dev']

run:
	export FLASK_ENV=development && \
	export FLASK_APP=mySite/app.py && \
	flask run

all: activate install run 