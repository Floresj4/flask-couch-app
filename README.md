# Flask/CouchDB web application

Using the Flask microframework and Jinja2 template renderer for python to develop a web application with simple document datastore interactions.

## docker-compose.yml

The container orchestration configuration script.  docker-compose.yml defines the 3 services used for this application: flask, couch, and couch-setup.  These 3 services are chained (depends_on) to ensure the CouchDB is created and configured before the `@app.route('/baseball')` route makes a request against it.

```sh
docker-compose up --build
```
builds the images before starting container services.

### _datastore

Contains Dockerfile and misc. configuration required to create the couchdb container image.

### _helper

Contains Dockerfile and misc. configuration required to configure the couchdb container shortly after startup.  See docker-compose.yml.

**load.py** executes a series of requests against the couch service creating the database, loading some data, and creating a view to query against.

### _service

Contains Dockerfile and misc. configuration required to create the flask container image.

**service.py** is the api service entrypoint.

## service.py

[service.py](https://github.com/Floresj4/flask-couch-app/blob/master/service.py "Flask entry point") has several endpoints to exercise basic API operations with the flask framework and CouchDB.  A browser client is available [here](http://localhost:5000) after cloning this repository and issuing the **docker-compose up** command.

## ~~service.bat~~

Deprecated, but worth mentioning... service.bat is docker-compose before I started working with compose.

1. ***-build** create the service container - flask or couch
2. ***-run** runs the container image

## ~~local~~

Runs the Flask app on the host windows machines. local requires the proper Python configuration to run this application on your local machine.  Using a virtual environment helps to avoid contaminating the native python installed libraries.  

The following commands will create and activate a virtual environment.

```sh
> python -m virtualenv .\env
> .\env\Scripts\activate
```

Once activated, the required libraries can be installed using the requirements.txt file in the root directory.

```sh
> pip install -r requirements.txt
```

Open your browser and navigate to `localhost:5000`.