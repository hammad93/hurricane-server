'''
Creates the required files for the Geographical Information System (GIS)
'''
import subprocess
import requests
import shutil

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
    process = subprocess.Popen(command, shell=True)
    process.wait()
    return output

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
    response = requests.get(url, stream=True, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    })
    chunk_unit = 1024 # bytes
    with open(path + filename, "wb") as file:
        # chunked by 1 MB
        for chunk in response.iter_content(chunk_size=1000 * chunk_unit):
            file.write(chunk)
    print('Done!')
    return path + filename # output path

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
    data = requests.get(url)
    with open(path + filename, "wb") as file:
        file.write(data.content)
    print('Done!')
    return path + filename # output path

def main(output_path='../wms_data/'):
    '''
    Processes the GIS files
    '''
    # download Blue Marble
    bm_out = blue_marble()
    # transform
    tiff_out = img_to_tiff(bm_out)
    # copy it over
    shutil.copy(tiff_out, output_path)

    # download coastlines
    coast_out = coastlines()
    # copy it over
    shutil.copy(coast_out, output_path)