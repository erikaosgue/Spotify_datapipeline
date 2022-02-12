FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY src/ .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install kafka-python
RUN pip install spotipy


RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]


