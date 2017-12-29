import glob
import os
import shutil
import random


pathMain = ['train','test']
pathClass = ['Bug','Invalid']
testData  = 150
listfileAll = []
listFile = []

if not os.path.exists('test'):
    os.makedirs('test')

for classFile in pathClass:
    print(classFile)
    i = 0
    listfileAll = glob.glob(pathMain[0] + '\\' + classFile + '\\' + '*.txt')
    #print (len(list))
    #fileAll = len(glob.glob(pathMain[0]+'/'+classFile+'/' + '*.txt'))
    #print (fileAll)
    
    #listfileAll = random.choice(list)
    listFile = random.sample(listfileAll, testData)
    
    for fileName in listFile:
        nFile = fileName.replace(str(pathMain[0]), '')
        print (nFile)
        shutil.move(fileName, pathMain[1] + nFile)
        #print(fileName)
