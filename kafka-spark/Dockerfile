
FROM docker.io/bitnami/spark:3

WORKDIR /opt/bitnami/spark/work


COPY requirements.txt ./
COPY src/ .

USER root
RUN pip install --no-cache-dir -r requirements.txt
RUN cp /opt/bitnami/spark/conf/log4j.properties.template /opt/bitnami/spark/conf/log4j.properties
RUN sed -i '0,/=INFO/s//=WARN/' /opt/bitnami/spark/conf/log4j.properties


RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]

