#!/bin/bash

cd ./docker

# run discord-bot
docker exec bot ts-node-dev --poll /usr/srb4/scripts/main.ts