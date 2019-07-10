FROM nginx:latest

RUN cd /etc/ssl
RUN apt-get update
RUN apt-get install openssl
RUN openssl req -subj '/C=BR/ST=Bahia/L=Salvador/O=OrgName/OU=WebDev/CN=localhost' -x509 -nodes -days 3650 -newkey rsa:4096 -keyout /etc/ssl/key.key -out /etc/ssl/cert.crt
RUN yes | apt-get remove openssl