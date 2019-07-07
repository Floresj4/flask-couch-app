FROM centos:latest

#add the couch repository
WORKDIR /etc/yum.repos.d/
COPY ./_datastore/couchdb.repo .
RUN yum-config-manager --add-repo ./couchdb.repo

#get couch
RUN yum install -y epel-release
RUN yum install -y couchdb

#overwrite local configuration
COPY _datastore/opt/couchdb/etc/local.ini /opt/couchdb/etc/

EXPOSE 5984

ENTRYPOINT /opt/couchdb/bin/couchdb