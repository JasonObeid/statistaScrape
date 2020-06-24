import os
import pandas as pd
import weasyprint as wsp
import PIL as pil
import matplotlib.pyplot as plt
import csv

def getChartType(x):
    if x.lower() == 'year':
        return 'line_chart'
    else:
        return 'bar_chart'


def trim(source_filepath, target_filepath=None, background=None):
    if not target_filepath:
        target_filepath = source_filepath
    img = pil.Image.open(source_filepath)
    if background is None:
        background = img.getpixel((0, 0))
    border = pil.Image.new(img.mode, img.size, background)
    diff = pil.ImageChops.difference(img, border)
    bbox = diff.getbbox()
    img = img.crop(bbox) if bbox else img
    img.save(target_filepath)


def openCaption(captionPath):
    with open(captionPath, 'r', encoding='utf-8') as captionFile:
        caption = captionFile.read()
    return caption


def openData(dataPath):
    df = pd.read_csv(dataPath, index_col='Unnamed: 0')
    df.rename(columns={'Unnamed: 0': '.'}, inplace=True)
    xAxis = 'unknown'#df.index.tolist()
    yAxis = df.columns[0]
    chartType = getChartType(xAxis)
    return df, xAxis, yAxis, chartType


dataFiles = os.listdir('./unlabelled/data')
dataFiles.sort()
# dataFiles = dataFiles[3800:4800]

captionFiles = os.listdir('./unlabelled/captions')
captionFiles.sort()
# captionFiles = captionFiles[3800:4800]

titleFiles = os.listdir('./unlabelled/titles')
titleFiles.sort()

assert len(captionFiles) == len(dataFiles) == len(titleFiles)

csvPath = "./unlabelled/data.csv"
with open(csvPath, mode='a', newline='') as csvFile:
    csvWriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
    csvWriter.writerow(["caption", "yAxis", "title", "imgPath"])
    for i in range(len(dataFiles)):
        dataPath = './unlabelled/data/' + dataFiles[i]
        captionPath = './unlabelled/captions/' + captionFiles[i]
        titlePath = './unlabelled/titles/' + titleFiles[i]
        caption = openCaption(captionPath).strip()
        title = openCaption(titlePath).strip()
        df, xAxis, yAxis, chartType = openData(dataPath)
        imgPath2 = './unlabelled/images/chart/' + dataFiles[i][:-3] + 'png'
        imgPath = './unlabelled/images/table/' + dataFiles[i][:-3] + 'png'
        """
        css = wsp.CSS(string='''
        @page { size: 2048px 2048px; padding: 0px; margin: 0px; }
        table, td, tr, th { border: 1px solid black; }
        td, th { padding: 4px 8px; }
        ''')
        html = wsp.HTML(string=df.to_html())
        html.write_png(imgPath, stylesheets=[css])
        trim(imgPath)
        """
        newCol = []
        for value in df.values:
            if str(value[0]) != '-':
                new_string = float(''.join(ch for ch in str(value[0]) if ch.isdigit() or ch == '.'))
            else:
                new_string = 0
            newCol.append(new_string)
        df.pop(df.columns[0])
        df[yAxis] = newCol
        print(df)
        if chartType == 'line_chart':
            ax = df.plot.line()
            ax.set_ylabel(yAxis)
        else:
            ax = df.plot.bar()
            ax.set_ylabel(yAxis)
        plt.savefig(imgPath2, bbox_inches="tight")
        plt.close()

        webPath = 'https://chart2text.s3.amazonaws.com/' + dataFiles[i][:-3] + 'png'
        line = (caption, yAxis, title, webPath)
        csvWriter.writerow(line)
