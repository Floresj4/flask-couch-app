@echo off

IF "%1"=="build" GOTO build
IF "%1"=="run" GOTO run
GOTO error

:build
docker build -t flask-app:latest .
GOTO finish

:run
docker run -it -p 5000:5000 --rm flask-app:latest
GOTO finish

:error
echo "'build' and 'run' are the only supported commands."

:finish