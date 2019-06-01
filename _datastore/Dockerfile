FROM centos:latest

#add the couch repository
WORKDIR /etc/yum.repos.d/
COPY ./_datastore/couchdb.repo .
RUN yum-config-manager --add-repo ./couchdb.repo

RUN yum install -y epel-release
RUN yum install -y couchdb