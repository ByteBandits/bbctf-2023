FROM ubuntu:22.04

RUN apt-get update -y && apt-get install -y \
    python3-pip \
    python3-dev \
    ucspi-tcp

WORKDIR /ctf

COPY . .

CMD ["tcpserver", "0.0.0.0", "9999", "python3", "chal.py"]

EXPOSE 9999