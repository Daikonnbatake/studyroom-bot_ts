#!/bin/bash

cd ./.docker

# run 
docker exec -i api /bin/bash -c "cd /usr/srb3/source && uvicorn main:app --reload --host 0.0.0.0 --port 8000"