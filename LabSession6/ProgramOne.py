import os
currentDirectory = os.path.dirname(__file__)
FILE_NAME = f"{currentDirectory}\\file.txt"

wordCounts = {}
fileHandler = open(FILE_NAME, 'r')

def removePunctuations(string):
    PUNCTUATIONS = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in string:
        if ele in PUNCTUATIONS:
            string = string.replace(ele, "")
    return string


for line in fileHandler:
    line = removePunctuations(line).lower()
    for word in line.split():
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1
                
lst = []
for key, val in list(wordCounts.items()):
    lst.append((val, key))
lst.sort(reverse=True) 
finalList = []
for val, key in lst:
    finalList.append((key, val))
print(dict(finalList[:10]))