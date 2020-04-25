# Import what's needed
from bs4 import BeautifulSoup
import os
import requests
from pathlib import Path

# Inputs cannot be empty
def getInput(text):
    x = input(text)
    if not x:
        getInput(text)
    else:
        return x

# Our base url where files and sub-directories are located
# Script will download every file with the given extension(s)
# and if you want it to go through sub-directories it also will
# do that
urlInput = getInput('Enter a URL to scape: ')

# Download directory
dirInput = getInput('Enter directory name: ')

# Our download directory where all the files will be stored 
# This is basically the script location and the download directory within
downloadDir = os.getcwd() + '\\' + 'download' + '\\' + dirInput + '\\'

# Extensions list (the files we want)
extsInput = getInput('Enter extensions to download (comma separated or *): ')
exts = extsInput.split(',')
exts = [item.strip() for item in exts]

# Exclude's are link text's we want to ignore
excludesInput = getInput('Enter excludes list (comma separated): ')
excludes = excludesInput.split(',')
excludes = [item.strip() for item in excludes]

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

        # Exclude?
        if text.lower() in excludes:
            continue

        # Download or iterate to next directory
        if (href.endswith('/')):
            run(url + href, dest + text + '\\')
        elif hrefExt in exts or '*' in exts:
            downloadFile(url+href, dest+text)

# Download file function
def downloadFile(url, dest):
    file = requests.get(url)
    open(dest, 'wb').write(file.content)
    print('Downloaded: ' + url)

run(urlInput, downloadDir)