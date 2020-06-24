import os
import pandas as pd
from shutil import copy

fileList = os.listdir('unlabelled/data')
count = 0
for filePath in fileList:
    textPath = filePath[0:len(filePath)-3] + 'txt'
    df = pd.read_csv('unlabelled/data/'+filePath)
    xAxis = df.columns[0]
    if xAxis == 'Unnamed: 0' or xAxis == '':
        copy('captions/' + textPath, 'unlabelled/captions/' + textPath)
        count += 1
    #else:
        #copy('captions/'+textPath, 'clean/captions/' + textPath)
        #df.to_csv(index=False, path_or_buf=('clean/data/'+filePath))
print(count)

# 1117 original, dhruv 830
