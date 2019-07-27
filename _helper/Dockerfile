FROM centos:latest

RUN yum install -y epel-release
RUN yum install -y python36
RUN yum install -y python36-pip

WORKDIR /app
COPY ./_helper/data ./data
COPY ./_helper/ .
RUN chmod 222 ./data/

RUN python36 -m pip install -r requirements.txt
# ENTRYPOINT python36 ./load.py