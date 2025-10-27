'''
Hammad Usmani
10/27/2025

Creates the required files for the Geographical Information System (GIS).

Requirements
------------
gdal_translate
'''
import subprocess
import requests
import sys
import os

def img_to_tiff(path, out='', proj='WGS84', cords='-180 +90 +180 -90'):
    '''
    Takes in the image file (e.g. JPG or PNG) and converts it to a GeoTIFF
    file. Additional parameters include the projection and coorindate plane.
    We utilize the gdal_translate command to achieve this.

    Parameters
    ----------
    path string
        The path to the image
    out string
        The output path for the tiff
    proj string
        The projection code
    cords string
        The coordinates for the -a_ullr command
    '''
    filename = path.split('/')[-1][:path.rfind('.')] + '.tiff' # create output path
    output_path = out + filename
    if check_file(output_path):
        return output_path
    command = f"gdal_translate -a_srs {proj} -a_ullr {cords} {path} {output_path}"
    process = subprocess.Popen(command, shell=True)
    process.wait()
    return output_path

def blue_marble(path='./', url='https://upload.wikimedia.org/wikipedia/commons/2/23/Blue_Marble_2002.png'):
    '''
    Downloads NASA's Blue Marble image from either the specified or configured URL

    Parameters
    ----------
    path string
        The path to save out to. Default is current directory
    url string
        The URL if configuring it other than the specified default

    References
    ----------
    - https://commons.wikimedia.org/wiki/File:Blue_Marble_2002.png
    '''
    print('Downloading Blue Marble . . . ')
    filename = url.split('/')[-1] # e.g. Blue_Marble_2002.png
    output_path = path + filename
    if check_file(output_path):
        return output_path
    response = requests.get(url, stream=True, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    })
    chunk_unit = 1024 # bytes
    with open(output_path, "wb") as file:
        # chunked by 1 MB
        for chunk in response.iter_content(chunk_size=1000 * chunk_unit):
            file.write(chunk)
    print('Done!')
    return output_path # output path

def coastlines(path='./', url='https://github.com/simonepri/geo-maps/releases/latest/download/countries-coastline-250m.geo.json'):
    '''
    Downloads the coastlines and other borders from either the specified or configured URL

    Parameters
    ----------
    path string
        The path to save out to
    url string
        Configurable URL compared to the default found in the references

    References
    ----------
    - https://github.com/simonepri/geo-maps/blob/master/info/countries-coastline.md
    '''
    print('Downloading GeoJSON . . . ')
    filename = url.split('/')[-1] # e.g. countries-coastline-250m.geo.json
    output_path = path + filename
    if check_file(output_path):
        return output_path
    data = requests.get(url)
    with open(output_path, "wb") as file:
        file.write(data.content)
    print('Done!')
    return output_path

def check_file(path):
    '''
    Given the path, this function checks if it exists.
    Use cases are to avoid costly downloads or transformations.
    '''
    exists = os.path.exists(path)
    if exists:
        print(f'Path {path} already exists')
    return exists

def main(out='../wms_data/'):
    '''
    Processes the GIS files. Used with a command line parameter.

    Example
    -------
    >>> python gis/gis.py -o ./wms_data/
    '''
    # download Blue Marble
    bm_out = blue_marble(path=out)
    # transform
    tiff_out = img_to_tiff(path=bm_out, out=out)

    # download coastlines
    coast_out = coastlines(path=out)

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        if arg == '-o':
            main(sys.argv[i + 1])
            print('Done Processing GIS files.')
            break