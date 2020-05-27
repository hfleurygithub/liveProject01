import os
import sys

def getfiles(path):
    files = []
    for dirpath, _, filenames in os.walk(path):
        for file in filenames:
            if file.endswith('.pdf'):
                files.append(os.path.join(dirpath, file))
    return files

for file in getfiles("."):
    print(file)