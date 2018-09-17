#FROM python:3
FROM ubuntu
RUN mkdir -p /web/server/test/
COPY . /web/server/test
RUN apt-get update -y
RUN apt-get install python3.6 -y
RUN apt-get install tcpdump -y
RUN apt-get install python3-pip -y
RUN pip3 install scapy
CMD python3 /web/server/test/src/dashbutton/dashButton.py

EXPOSE 8080