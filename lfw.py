import shutil
import os
import re

cwd = os.getcwd()

def moveFiles():
    for folder, _, files in os.walk(cwd):
        if folder == cwd:
            continue
        for i in files:
            shutil.move(os.path.join(folder, i), os.path.join(cwd, i))

    for folder, _, files in os.walk(cwd):
        if folder == cwd:
            continue
        os.rmdir(folder)

def generateList():
    i = 0
    n = 10000
    pattern = re.compile(".jpg$")
    output = open("./train.list", mode ="w")
    for f in os.listdir(cwd):
        if pattern.search(f):
            output.write(f)
            output.write("\n")
            i +=1
            if i == n:
                output.close()
                output = open("./test.list", mode ="w")
    print(i)
    output.close()
