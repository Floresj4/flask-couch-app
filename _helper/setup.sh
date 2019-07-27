#!/bin/sh

#sleep to give the couch container time to start
sleep 5

#create database
curl -XPUT http://couch:5984/baseball?n=1

#-- add a document
curl -ik -XPOST -H "Content-Type: application/json" http://couch:5984/baseball/_bulk_docs -d ./data/@data-00.json

#-- get a document
#curl -ik -XGET http://couch:5984/baseball/57a357df16f446381db1330844000532

#-- get database info
#curl -ik -XGET http://couch:5984/baseball