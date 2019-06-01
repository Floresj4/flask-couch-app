## Flask web application/service

A checklist project &ndash; create an application or api &ndash; using the Flask microframework for learning a new technology and some nerdy computer fun!

### Setup

Using a virtual environment helps to avoid contaminating the native python installed libraries.  The following commands will create and activate a virtual environment.

```sh
> python -m virtualenv .\env
> .\env\Scripts\activate
```

Once activated, the required libraries can be installed using the requirements.txt file in the root directory.

```sh
> pip install -r requirements.txt
```

### service.bat

service.bat provides convenience routines to build and deploy the application on a windows machine.

1. **docker-build** creates a container image to run the application in a hosted environment
2. **docker-run** runs the container image
3. **local runs** the flask application on the host windows machines
