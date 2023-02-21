#!/bin/sh

cp database.key docker/
cp django_secret.key docker/
git clone --single-branch --branch main https://github.com/hammad93/hurricane-deploy.git
cp credentials.csv ./hurricane-deploy/docker/
git clone --single-branch --branch master https://github.com/apatel726/HurricaneDissertation.git
docker-compose build --no-cache
docker-compose up
