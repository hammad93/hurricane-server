FROM continuumio/anaconda3:2020.07

# Python additional requirements

COPY requirements.txt /root/
RUN pip install -r /root/requirements.txt

# Add git repository

RUN git clone --single-branch --branch master https://github.com/hammad93/hurricane-server.git
RUN git clone --single-branch --branch master https://github.com/hammad93/hurricane-map.git

# Web server and Database keys
COPY database.key ./hurricane-map/django/map/map/keys/
COPY django_secret.key ./hurricane-map/django/map/map/keys/

# Setup cron job

RUN apt-get update && apt-get -y install cron

# Entrypoint
ADD entrypoint.sh /root/entrypoint.sh
RUN chmod +x /root/entrypoint.sh
ENTRYPOINT /root/entrypoint.sh
