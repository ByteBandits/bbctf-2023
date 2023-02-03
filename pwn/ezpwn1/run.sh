#!/bin/bash

docker build . -t ez-pwn-1
docker run -d -p ${HOST_PORT}:8000 ez-pwn-1