# hurricane-server
Hello! This server hosts the hurricane artificial intelligence that can be accessed through the
link https://github.com/hammad93/hurricane-net . The domain name configured is https://fluids.ai

## Quickstart

- Run the command `sudo bash start.sh` to setup and start the orchestration of the containers
- Run the command `sudo bash stop.sh` to stop the containers.

## Renew SSL (HTTPS)

Visit https://certbot.eff.org/ for more details.

-  Ensure `certbot` is installed with `sudo apt install certbot`.
-  Ensure the domain name's DNS records are pointing to the IP address `hurricane-server` is running on.

1. If `hurricane-server` is setup correctly, it is utilizing port 80. Stop `hurricane-server` by running the `sudo bash ./stop.sh` script in this repository so `certbot` can use the port to test the domain name.
2. Run `sudo certbot certonly --standalone` to process the SSL files (fullchain, privkey). Enter in the domain names from earlier. We copy these files manually. Note save directory for SSL files (/etc/letsencrypt/live/...)
3. Create a directory named ssl like so, `mkdir ./docker/proxy/ssl`
4. Copy the `fullchain.pem` and `privkey.pem` files from the save directory in step 2.
5. Rebuild `hurricane-server` by running `sudo bash ./stop.sh`


## Environment Variables
Place the `.env` file in this directory (`./`) that the `docker-compose.yml` utilizes.
