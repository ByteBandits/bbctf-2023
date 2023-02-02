FROM ubuntu:22.04

RUN apt-get update -y && apt-get install -y \
    python3-pip \
    python3-dev \
    ucspi-tcp

WORKDIR /ctf

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

