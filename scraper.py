# Import what's needed
from bs4 import BeautifulSoup
import os
import requests
from pathlib import Path

# Our base url where files and sub-directories are located
# Script will download every file with the given extension(s)
# and if you want it to go through sub-directories it also will
# do that
urlInput = input('Enter a URL to scape: ')

# Download directory
dirInput = input('Enter directory name: ')

# Our download directory where all the files will be stored 
# This is basically the script location and the download directory within
downloadDir = os.getcwd() + '\\' + 'download' + '\\' + dirInput + '\\'

# Extensions and exclude list
# Extensions are files we want to download
# Exclude's are link text's we want to ignore
exts = ['.mod', '.it', '.xm']
excludes = ['parent directory', '..', '.', 'MODLAND']

# Dowload given URL
# to given destination directory
def run(url, dest):

    # Grab page
    request = requests.get(url)

    # Create destination directory
    Path(dest).mkdir(parents = True, exist_ok = True)

    # Parse the HTML data
    html = request.text
    soup = BeautifulSoup(html)

    # Go through every link
    for link in soup.find_all('a'):

        # Grab href and link text (for naming purpose)
        href = link.get('href')
        text = link.text.strip()

        # Grab the file extension from the URL
        hrefExt = os.path.splitext(href)[1]

        # Check that the file in this iteration is
        # in the extensions list
        # Do some excludes
        if text.lower() in excludes:
            continue
        elif hrefExt in exts:
            downloadFile(url+href, dest+text)
            #file = requests.get(url + href)
            #open(dest + text, 'wb').write(file.content)
            #print('Downloaded: ' + url+text)

        elif (href.endswith('/')):
            run(url + href, dest + text + '\\')

# Download file function
def downloadFile(url, dest):
    file = requests.get(url)
    open(dest, 'wb').write(file.content)
    print('Downloaded: ' + url)

run(urlInput, downloadDir)

