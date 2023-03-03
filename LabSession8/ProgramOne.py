# Develop a program to read the contents of a text file, sort contents read and write the sorted contents into a separate text file

import os
currentDirectory = os.path.dirname(__file__)
PATH = f"{currentDirectory}\\read.txt"
with open(PATH) as f:
    content = f.read()
    content = content.split("\n")
    content.sort()
    file = open(f"{currentDirectory}\\write.txt", "w")
    for word in content:
        file.write(f"{word}\n")
    file.close()
print("Program executed. Check write.txt")