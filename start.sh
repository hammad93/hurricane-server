#!/bin/sh

#echo "Creating wms data directory if it doesn't exist."
#mkdir -p wms_data
#docker image prune -f
#git clone --depth 1 --single-branch --branch main https://github.com/hammad93/hurricane-deploy.git
#git clone --depth 1 --single-branch --branch master https://github.com/apatel726/HurricaneDissertation.git
#git clone --depth 1 --single-branch --branch main https://github.com/hammad93/hurricane-geoserver.git
#cp database.key docker/
#cp django_secret.key docker/
#cp hurricane-live-db.key docker/
#cp credentials.csv ./hurricane-deploy/docker/
#docker compose build --no-cache
docker compose up
