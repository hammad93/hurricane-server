# hurricane-server
Provides a Dockerized solution to host a Tensorflow Deep Learning Model specially for hurricane research. 

The intent of this repository is to open source everything available through https://fluids.ai

## Installation & Quickstart

Run the following command on a Linux system with Docker installed,
`sh ./run.sh`

To rebuild, first remove the containers,
`sudo docker-compose rm -f -s`

Then prune. This will allow us to rebuild from start
`sudo docker image prune -a`

We can see the logs with this command,
`sudo docker-compose logs`

## Credentials

There's a few credential files that's needed for the `hurricane-deploy` repository. Place it in the root of this repository, `./`

 - credentials.csv
 - database.key
 - django_secret.json

## Ports

### 1337

The REST API is located here.

### 7000

This hosts the interactive map

### 6005

This is the Jupyter Lab environment available for developers.

### 6006

When testing out machine learning models, this port allows access to a web application describing the progress of training and comparisons utilizing TensorBoard or other framework.
