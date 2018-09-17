FROM python:3
RUN mkdir -p /web/server/test/
COPY . /web/server/test
RUN pip3 install scapy
CMD python3 /web/server/test/src/dashbutton/dashButton.py

EXPOSE 8080