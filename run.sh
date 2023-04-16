#!/bin/sh

docker image prune -f
cp database.key docker/
cp django_secret.key docker/
cp hurricane-live-db.key docker/
git clone --single-branch --branch main https://github.com/hammad93/hurricane-deploy.git
cp credentials.csv ./hurricane-deploy/docker/
git clone --depth 1 --single-branch --branch master https://github.com/apatel726/HurricaneDissertation.git
docker-compose build --no-cache
docker-compose up
