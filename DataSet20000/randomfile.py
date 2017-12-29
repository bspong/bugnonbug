import os
import random

def getRandomFile(path):
    files = os.listdir(path)
    index = []
    index = random.randrange(0, len(files),3)
    return files[index]

path = ['train/bug/','invalid/']

x = []
x = getRandomFile(path[0])
print (len(x))
trainFile = 10000
testFile = 2000
# for


# print (getRandomFile(path))
