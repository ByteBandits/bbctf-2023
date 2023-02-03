#!/bin/bash

docker build . -t ez-pwn-2
docker run -d -p ${HOST_PORT}:8000 ez-pwn-2