import os
import re
from shutil import copyfile
from selenium import webdriver
from PIL import Image
from io import BytesIO
from time import sleep
import base64
import pandas as pd

browser = webdriver.Chrome(executable_path='/home/jason/chromedriver')
scraped = pd.read_csv('multiColumn/otherMetadata.csv')

for row in scraped.iterrows():
    cleanUrl = row[1].URL
    browser.get(cleanUrl)
    sleep(4)
    image = browser.find_element_by_class_name('statisticHeader').screenshot_as_png
    im = Image.open(BytesIO(image))  # uses PIL library to open image in memory
    im.save(f'multiColumn/images/{row[1].id}.png')