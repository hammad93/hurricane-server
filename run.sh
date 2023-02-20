#!/bin/sh

git clone --single-branch --branch main https://github.com/hammad93/hurricane-deploy.git
git clone --single-branch --branch master https://github.com/apatel726/HurricaneDissertation.git
docker-compose up
