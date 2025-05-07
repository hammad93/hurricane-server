#!/bin/bash

# Description: Simplified script to obtain and install Let's Encrypt SSL certificates using Certbot.

DOMAIN="nfc.ai"
EMAIL="husmani@fluids.ai"

# Install Certbot if not installed
if ! command -v certbot &> /dev/null; then
    echo "Certbot not found. Installing..."
    sudo apt-get update
    sudo apt-get install -y certbot python3-certbot-nginx
fi

# Obtain SSL certificate
sudo certbot --nginx -d "$DOMAIN" --non-interactive --agree-tos -m "$EMAIL"

# Reload Nginx to apply changes
sudo systemctl reload nginx

echo "Let's Encrypt SSL certificate has been installed and Nginx reloaded."