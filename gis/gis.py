'''
Creates the required files for the Geographical Information System (GIS)
'''
import subprocess
import requests

def img_to_tiff(path, proj='WGS84', cords='-180 +90 +180 -90'):
    '''
    Takes in the image file (e.g. JPG or PNG) and converts it to a GeoTIFF
    file. Additional parameters include the projection and coorindate plane.
    We utilize the gdal_translate command to achieve this.

    Parameters
    ----------
    path string
        The path to the image
    proj string
        The projection code
    cords string
        The coordinates for the -a_ullr command
    '''
    output = path[:path.rfind('.')] + '.tiff' # create output path
    command = f"gdal_translate -a_srs {proj} -a_ullr {cords} {path} {output}"
    subprocess.Popen(command, shell=True)

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
    filename = url.split('/')[-1] # e.g. Blue_Marble_2002.png
    response = requests.get(url, stream=True)
    chunk_unit = 1024 # bytes
    with open(path + filename, "wb") as file:
        for chunk in response.iter_content(chunk_size=1000 * chunk_unit):
            file.write(chunk)

def coastlines(path='./', url=''):
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