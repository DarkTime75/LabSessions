import os
currentDirectory = os.path.dirname(__file__)
FILE_NAME = f"{currentDirectory}\\file.txt"

word_counts = {}

def second(ele):
    return ele[1]

def removePunctuations(string):
    PUNCTUATIONS = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in string:
        if ele in PUNCTUATIONS:
            string = string.replace(ele, "")
    return string

with open(FILE_NAME, 'r') as file:
    for line in file:
        line = removePunctuations(line).lower()
        for word in line.split():
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
                
lst = list(word_counts.items())
lst.sort(key = second, reverse = True)
print(dict(lst[:10]))