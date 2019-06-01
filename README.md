### Flask web application/service

A checklist project &ndash; create an application or api &ndash; using the Flask microframework for learning a new technology and some nerdy computer fun!

##### Setup

Using a virtual environment helps to avoid contaminating the native python installed libraries.  The following commands will create and activate a virtual environment.

```sh
> python -m virtualenv .\env
> .\env\Scripts\activate
```

Once activated, the required libraries can be installed using the requirements.txt file in the root directory.

```sh
pip install -r requirements.txt
```

##### Running on windows

```sh
> set FLASK_APP=service.py
> python -m flask run
```

##### Running on linux

```sh
> export FLASK_APP=service.py
> python -m flask run
```

##### Running with Docker

This project provides a Dockerfile to build and run