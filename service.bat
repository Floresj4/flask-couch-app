@echo off

IF "%1"=="couch-build" GOTO couch-build
IF "%1"=="couch-run" GOTO couch-run
IF "%1"=="service-build" GOTO docker-build
IF "%1"=="service-run" GOTO docker-run
IF "%1"=="local" GOTO local
GOTO error

:couch-build
rem build and tag the latest couchdb image
docker build -f ./_datastore/Dockerfile -t couchdb-api:latest .
GOTO finish

:couch-run
rem start the container and ensure it's removable on exit
docker run -it -p 5984:5984 --rm couchdb-api:latest
GOTO finish

:service-build
rem build and tag the latest service image
docker build -f ./_service/Dockerfile -t flask-app:latest .
GOTO finish

:service-run
rem start the container and ensure it's removable on exit
docker run -it -p 5000:5000 --rm flask-app:latest
GOTO finish

:local
rem run the flask application locally
set FLASK_APP=service.py
set FLASK_ENV=development
flask run --host=0.0.0.0
GOTO finish

:error
echo "'docker-build', 'docker-run', and 'local' are the only supported commands."

:finish