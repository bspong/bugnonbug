import glob
import os


pathMain = 'train'
pathClass = ['Bug','Invalid']

if not os.path.exists('test1'):
    os.makedirs('test1')

for classFile in pathClass:
    print(classFile)
    fileAll = len(glob.glob(classFile+'/' + '*.txt'))

#
