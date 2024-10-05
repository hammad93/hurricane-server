FROM continuumio/anaconda3

# Python additional requirements

COPY requirements.txt /root/
RUN pip install -r /root/requirements.txt

# Add git repository
RUN git clone --single-branch --branch main https://github.com/hammad93/hurricane-server.git
RUN git clone --single-branch --branch main https://github.com/hammad93/hurricane-map.git

# Web server and Database keys
COPY credentials.csv ./hurricane-map/django/map/map/keys/
COPY django_secret.key ./hurricane-map/django/map/map/keys/

# Entrypoint
ADD entrypoint.sh /root/entrypoint.sh
RUN chmod +x /root/entrypoint.sh
ENTRYPOINT /root/entrypoint.sh
