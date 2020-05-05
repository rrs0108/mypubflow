#!/bin/bash

SERVER_ADDR="localhost:8001"

rm -rf target && mkdir target
cp -R concord.yml *.py target/

cd target && zip -r payload.zip ./* > /dev/null && cd ..

#read -p "Username: " CURL_USER
curl -u myuser -F archive=@target/payload.zip http://${SERVER_ADDR}/api/v1/process
