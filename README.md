## Flask web application/service

A checklist project &ndash; create an application or api &ndash; using the Flask microframework for learning a new technology and some nerdy computer fun!

### service.bat

service.bat provides convenience routines to build and deploy the application on a windows machine.

1. **docker-build** creates a container image to run the application in a hosted environment
2. **docker-run** runs the container image
3. **local** runs the flask application on the host windows machines

### local

local requires the proper Python configuration to run this application on your local machine.  Using a virtual environment helps to avoid contaminating the native python installed libraries.  The following commands will create and activate a virtual environment.

```sh
> python -m virtualenv .\env
> .\env\Scripts\activate
```

Once activated, the required libraries can be installed using the requirements.txt file in the root directory.

```sh
> pip install -r requirements.txt
```

Open your browser an navigate to `localhost:5000`.


Couchdb creates files in the following locations

```sh
find / -name "couchdb"
/etc/logrotate.d/couchdb
/var/lib/couchdb
/var/log/couchdb
/opt/couchdb
/opt/couchdb/bin/couchdb
/opt/couchdb/var/log/couchdb
```

```sh
curl -ik http://localhost:5984/flask-app
curl -XPUT -H "Content-Type: application/json" -d '{ "name":"jason", "email":"jason@mail.com" }' http://localhost:5984/flask-app/sampledoc
curl -ik http://localhost:5984/flask-app/_all_docs
```