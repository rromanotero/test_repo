from python:3.8.3-slim-buster

RUN mkdir /app
RUN mkdir /tests

#Install
RUN apt-get -y update \
    && apt-get install python3-pip \
    && pip3 install --upgrade setuptools \
    && pip3 install --upgrade adafruit-python-shell \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

#Install reqs
COPY requirements /app
RUN python3 -m pip install -r /app/requirements

#Copy src and test
COPY /src /app
COPY /tests /tests

EXPOSE 5000

CMD [ "python3", "app/app.py" ]
