import os
import pandas as pd

fileList = os.listdir('2Columns')
count = 0
for filePath in fileList:
    df = pd.read_csv('2Columns/'+filePath)
    xAxis = df.columns[0]
    print(xAxis)
    if(xAxis == 'Unnamed: 0'):
        count += 1
print(count)
