# Flask web application/service

A checklist project &ndash; create an application or api &ndash; using the Flask microframework for learning a new technology and some nerdy computer fun!

## docker-compose.yml

The container orchestration configuration script.  docker-compose.yml defines the 3 services used for this application: flask, couch, and couch-setup.  These 3 services are chained (depends_on) to ensure the CouchDB is created and configured before the interactive REST service makes a request against it.

### ~~service.bat~~

Deprecated, but worth mentioning... service.bat is docker-compose before I started working with compose.

1. ***-build** create the service container - flask or couch
2. ***-run** runs the container image

#### ~~local~~

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

### service.py

[service.py](https://www.google.com "Flask entry point") has several endpoints to exercise basic API operations with the flask framework and CouchDB.  A browser client is available [here](http://localhost:5000).
