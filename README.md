# hurricane-server
Hello! This server hosts the hurricane artificial intelligence that can be accessed through the
link https://github.com/hammad93/hurricane-net . The domain name configured is https://fluids.ai

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

Hurricane Map
-------------
There is a MySql database called hurricane_archive that is utilized by the same instance 
as WordPress.

Here is the startup script for the hurricane map
/opt/bitnami/apps/wordpress/htdocs/map/hurricane-map/django/map$ python3 manage.py runserver 0.0.0.0:7000

SSL Certificate
---------------
To renew the certificate, we use certbot. We have to bring down the server and start
it back up using this command,

sudo /opt/bitnami/ctlscript.sh stop

This is the certbot command to renew,

sudo certbot renew

To start it back up,

sudo /opt/bitnami/ctlscript.sh start
## Ports

### 1337
The REST API is located here.

### 7000
This hosts the interactive map

### 6005
This is the Jupyter Lab environment available for developers.

### 6006
When testing out machine learning models, this port allows access to a web application describing the progress of training and comparisons utilizing TensorBoard or other framework.
