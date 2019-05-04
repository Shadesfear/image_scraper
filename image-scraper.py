import urllib.request
from urllib.request import urlretrieve
import os

import re


def find_images(URL):
    print("Scraping images from: ", URL)

    fp = urllib.request.urlopen(URL)
    source = fp.read().decode("utf8")

    regex_string = "(?<=<div class=\"gallery-image-covered js-gallery-image-covered\" data-src=\")(.*)(?=\"><\\/div>)"

    urls = re.findall(regex_string, source)

    os.mkdir(URL.split("/")[-1]);


    for idx, url in enumerate(urls):
        try:
            urlretrieve(urls[idx], URL.split("/")[-1]+"/"+str(idx)+".jpg")
        except:
            continue

    fp.close()


if __name__=="__main__":
    find_images("https://home.dk/sag/114J00208")
    find_images("https://home.dk/sag/643-00258")
