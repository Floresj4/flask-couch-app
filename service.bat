@echo off

IF "%1"=="docker-build" GOTO docker-build
IF "%1"=="docker-run" GOTO docker-run
IF "%1"=="local" GOTO local
GOTO error

:local
rem run the flask application locally
set FLASK_APP=service.py
set FLASK_ENV=development
flask run --host=0.0.0.0
GOTO finish

:docker-build
rem build and tag the latest Docker image
docker build -t flask-app:latest .
GOTO finish

:docker-run
rem start the container and ensure it's removable on exit
docker run -it -p 5000:5000 --rm flask-app:latest
GOTO finish

:error
echo "'build', 'run', and 'local' are the only supported commands."

:finish