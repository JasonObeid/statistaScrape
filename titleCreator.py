import os
import re
from scrapy import link
from shutil import copyfile

import pandas as pd

scraped = pd.read_csv('scraped.csv')
urlList = {}
for row in scraped.iterrows():
    for item in row[1].items():
        # print(item[1])
        text = re.search("text='(.*?)'", item[1])
        if text == None:
            text = re.search("text=\"(.*?)\"", item[1])
        url = re.search("url='(.*?)'", item[1])
        cleanText = text.group()
        cleanUrl = url.group()
        cleanText = cleanText[6:len(cleanText) - 1].strip()
        cleanUrl = cleanUrl[5:len(cleanUrl) - 1].strip()
        cleanText = re.sub("\s+", ' ', cleanText)
        urlList[cleanUrl] = cleanText

print(urlList["https://www.statista.com/statistics/248622/rates-of-leading-causes-of-death-in-the-us/"])
print(type(urlList))

fileList = os.listdir('temp/data')
metadata = pd.read_csv('metadata.csv')
count = 0
for filePath in fileList:
    rowIndex = int(filePath[0:len(filePath) - 4])
    row = metadata.iloc[rowIndex]
    title = urlList[row[6]]
    textPath = filePath[0:len(filePath)-3] + 'txt'
    with open(f'temp/titles/{textPath}', mode='wt', encoding='utf8') as myfile:
            myfile.write(title)
