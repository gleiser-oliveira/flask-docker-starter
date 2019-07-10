FROM python:latest

RUN mkdir /usr/src/app
COPY ./flaskapp/requirements.txt /usr/src/app/requirements.txt
COPY ./flaskapp/web_app.py /usr/src/app/web_app.py
COPY ./flaskapp/wsgi.py /usr/src/app/wsgi.py
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt
WORKDIR /usr/src/app