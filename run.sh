#!/bin/bash

cd ./.docker

# run discord-bot
docker exec bot npx ts-node-dev --poll /usr/srb3/source/scripts/main.ts