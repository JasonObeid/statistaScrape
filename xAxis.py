import os
import pandas as pd

fileList = os.listdir('2Columns')
count = 0
for filePath in fileList:
    df = pd.read_csv('2Columns/'+filePath)
    xAxis = df.columns[0]
    yAxis = df.columns[1]
    if(xAxis == 'Unnamed: 0' or xAxis == ''):
        print(filePath)
        fileName = filePath[0:len(filePath)-3] + 'txt'
        textPath = 'captions/' + fileName
        with open(textPath) as txt:
            print(txt.read())
        print('unrecognized column:')
        print(df.head())
        newXAxis = input('Replace with:')
        df.columns = [newXAxis, df.columns[1]]
        print("new table:")
        print(df.head())
        df.to_csv(index=False, path_or_buf=('2Columns/'+filePath))
    #else:
        #text = filePath[0:len(filePath)-3] + 'txt'
        #copyfile('2Columns/'+filePath, 'temp/data/'+filePath)
        #copyfile('captions/' + text, 'temp/captions/' + text)

#print(count)