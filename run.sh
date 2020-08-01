#!/bin/bash

set -ex

# docker kill and rm prevent funny errors
docker kill cherrypy > /dev/null 2>&1 || true
docker rm cherrypy > /dev/null 2>&1 || true

# build, test, and run the image
docker build -t simple-mongo-web-ui .
docker rm simple-mongo-web-ui-run || true
docker run -ti --name simple-mongo-web-ui-run -p 80:80 simple-mongo-web-ui $@
