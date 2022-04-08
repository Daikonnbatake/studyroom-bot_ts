#!/bin/bash

cd ./docker

# run discord-bot
docker exec bot npx ts-node-dev --poll /usr/srb4/source/scripts/main.ts