#!/bin/sh

#sleep to give the couch container time to start
sleep 5

#create database
curl -XPUT http://couch:5984/mydatabase?n=1

#-- add a document
#curl -ik -XPOST -H "Content-Type: application/json" http://localhost:5984/mydatabase -d @data-00.json

#-- add a document
#curl -ik -XPOST -H "Content-Type: application/json" http://localhost:5984/mydatabase -d @data-01.json

#-- get a document
#curl -ik -XGET http://localhost:5984/mydatabase/57a357df16f446381db1330844000532

#-- get database info
#curl -ik -XGET http://localhost:5984/mydatabase