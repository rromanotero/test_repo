from python:3.8.3-slim-buster

RUN mkdir /app
RUN mkdir /tests

#Install reqs
COPY requirements.txt /app
RUN python3 -m pip install -r /app/requirements

#Copy src and test
COPY /src /app
COPY /tests /tests

EXPOSE 5000

CMD [ "python3", "app/app.py" ]
