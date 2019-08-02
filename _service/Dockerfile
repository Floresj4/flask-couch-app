FROM centos:latest

RUN yum install -y epel-release
RUN yum install -y python36
RUN yum install -y python36-pip

#simlink the python executable
RUN ln -sf /usr/bin/python3.6 /usr/bin/python

#upgrade pip, just cause... and the flask dependency
RUN python -m pip install --upgrade pip
RUN python -m pip install requests
RUN python -m pip install flask

# set the relevant locale
ENV LANG en_US.UTF-8

#set application directory
WORKDIR /app

#move application files
COPY templates ./templates
COPY service.py .

#expose a mappable port
EXPOSE 5000

ENTRYPOINT flask run --host=0.0.0.0
