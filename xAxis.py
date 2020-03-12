import os
import pandas as pd
from shutil import copyfile

#todo 1152 manual annotations left

fileList = os.listdir('2Columns')
count = 0
for filePath in fileList:
    df = pd.read_csv('2Columns/'+filePath)
    xAxis = df.columns[0]
    yAxis = df.columns[1]
    if(xAxis == 'Unnamed: 0' or xAxis == ''):
        count += 1
        copyfile('2Columns/' + filePath, 'needsLabel/' + filePath)
        # print(filePath)
        # print('unrecognized column:')
        # print(df.head)
        # newXAxis = input('Replace with:')
        # df.columns = [newXAxis, df.columns[1]]
        # print(df.head())
        # df.to_csv(index=False, path_or_buf=('2Columns/'+filePath))
    #else:
        #text = filePath[0:len(filePath)-3] + 'txt'
        #copyfile('2Columns/'+filePath, 'temp/data/'+filePath)
        #copyfile('captions/' + text, 'temp/captions/' + text)

print(count)