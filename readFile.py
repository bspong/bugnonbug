import glob
import os
import io
import os.path
import re
import tarfile
import codecs
import sys



def fileRead(fileName):
    fileContents = open(fileName, 'r').read()
    return fileContents


def ReadAllinDir(pathFile):
    content_All=[]
    errorFile = 1
    for fileName in glob.glob(pathFile + '*.txt'):
        
        try:        
            fileContent = io.open(fileName,'r',encoding='utf8')
            content_All.append(fileContent.read())   
            fo = open('olo.txt', 'a')
            fo.write(fileContent.read())
            fo.close()
            fileContent.close()
            print ('readFile : '+ fileName )
           
        except :
            print('------- Num File Error : '+ str(errorFile) + '-----Can not Read File : ' + fileName + '-------')
            fileError = open('Error_ReadFile.txt','a')
            fileError.write(fileName+ ' \n')
            fileError.close()
            errorFile = errorFile + 1
    return content_All
  
def createOneFile(pathFile,fileClass):
    txtFile = []
    
    fo = open('TxT_' + fileClass + '.txt', 'a')
    for fileName in glob.glob(pathFile + '\\*.txt'):
            txtFile.append(open(fileName,'r').read())
            fo.write(str(txtFile))
    fo.close()


def readFile2():
    data_path = 'DataSet\\Bug\\'
    for filename in glob.glob(os.path.join(data_path, "*.txt")):
        print('ReadFile' + filename )
        doc = codecs.open(filename, 'rb', encoding='utf-8', errors='ignore').read()
        yield doc

# iii=0
# for i in readFile2():
#     print(i.encode('utf8').decode(sys.stdout.encoding))
#     iii=iii+1
#     print (iii)
# #    print()
# # readDoc = readFile2()
# # readDoc
# # readDoc.next()
# # # readFile2('DataSet\\Bug\\')
# # # readFile2.next()
# # print(readDoc.__next__)
# # # pathFile = 'DataSet/Bug/'
# # # ReadAllinDir(pathFile)
