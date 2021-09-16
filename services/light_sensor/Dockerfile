from python:3.8.3-slim-buster

RUN mkdir /app
RUN mkdir /tests

#Install Circuit Python Libraries
RUN pip3 install adafruit-circuitpython-ssd1306 \
    && pip3 install adafruit-circuitpython-framebuf \
    && pip3 install adafruit-circuitpython-rfm69

#Install reqs
COPY requirements /app
RUN python3 -m pip install -r /app/requirements

#Copy src and test
COPY /src /app
COPY /tests /tests

EXPOSE 5000

CMD [ "python3", "app/app.py" ]
