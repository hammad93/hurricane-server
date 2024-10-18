# hurricane-server
Hello! This server hosts the hurricane artificial intelligence that can be accessed through the
link https://github.com/hammad93/hurricane-net . The domain name configured is https://fluids.ai

## Installation & Quickstart
This repository is reproduceable. Please try from a new clone if there are errors or unexpected behaviors.

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

 - django_secret.json

## Hurricane Map
We utilize the fluids HTTP API to get the live storms and forecasts. Then, we plot them on an interactive map.

## SSL Certificate
We create standalone SSL certificates from LetsEncrypt and can renew them using this command,

`sudo certbot renew`

## Ports

### 1337 (Public)
The REST API is located here.

### 8000
This hosts the interactive map

### 6004
The Geoserver container with WMS capabilities.

### 6005
This is the Jupyter Lab environment available for developers.

### 6006
When testing out machine learning models, this port allows access to a web application describing the progress of training and comparisons utilizing TensorBoard or other framework.
