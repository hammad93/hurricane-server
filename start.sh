#!/bin/sh

echo "Creating wms data directory if it doesn't exist."
mkdir -p wms_data
echo "Processing GIS files."
apt update -y
apt-get install -y libgdal-dev gdal-bin python3-gdal
python3 gis/gis.py -o ./wms_data/
yes | docker system prune -a
docker compose build --no-cache
docker compose up -d
