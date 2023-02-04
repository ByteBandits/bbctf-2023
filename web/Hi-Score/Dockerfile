FROM ubuntu:22.04

RUN apt-get update -y && apt-get install -y \
    python3-pip \
    python3-dev \
    ucspi-tcp

WORKDIR /ctf

COPY . .

EXPOSE 8080

CMD [ "python3", "app.py"]

