from python:3.8.3-slim-buster

RUN mkdir /app
RUN mkdir /tests

#Install Circuit Python Libraries
RUN apt-get -y update \
  && apt -y update \
  && apt-get -y install python3-dev python3-rpi.gpio \
  && python3 -m pip install --upgrade pip setuptools wheel \
  && apt -y install build-essential \
  && pip3 install RPi.GPIO \
  && pip3 install adafruit-circuitpython-ssd1306 \
  && pip3 install adafruit-circuitpython-framebuf \
  && pip3 install adafruit-circuitpython-rfm69 \
  && rm -rf /var/lib/apt/lists/*

#Install reqs
COPY requirements /app
RUN python3 -m pip install -r /app/requirements

#Copy src and test
COPY /src /app
COPY /tests /tests

EXPOSE 5000

CMD [ "python3", "app/app.py" ]
