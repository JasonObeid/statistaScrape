import os

captionList = os.listdir('captions')
captionCount = 0
wordCountList = []

for filePath in captionList:
    with open('captions/'+filePath,'r') as caption:
        captionWords = caption.read().split()
        wordCount = len(captionWords)
        wordCountList.append(wordCount)
        captionCount += 1

averageWords = sum(wordCountList)/captionCount
print(averageWords)