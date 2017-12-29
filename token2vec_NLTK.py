from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

# def manageFile(fileName, Fmode, contents):
#     fo = open(fileName,Fmode)
#     if Fmode == 'r':
#         outPut = fo.read()
#     else:
#         for contents
#         fo.write()

def nltkWordToken(content):
    conTokened = word_tokenize(content)
    return conTokened
def wordLemmatizer(dataInput):
    wordLemma =[]
    lemmazer = WordNetLemmatizer()
    for word in dataInput:
        wordLem = lemmazer.lemmatize(word)
        #print (wordLem)
        wordLemma.append(wordLem)
    return wordLemma
    #return wordLemma
    

fo = open('test.txt','r')
x = fo.read()
fo.close()
conTokened = nltkWordToken(x)
#print (conTokened)
conLemma = wordLemmatizer(conTokened)
fo = open('lemaED.txt', 'w')
for word in conLemma:
    fo.write(word+'\n')
fo.close()
print('Complete !!!')
#print (conLemma)
#wordLem = WordNetLemmatizer()
#print (wordlem.lemmatize('cars'))
#print(wordLem.lemmatize("used", pos="v"))
#print(wordLem.lemmatize('users'))
