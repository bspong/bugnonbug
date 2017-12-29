from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfVectorizer
from sklearn.feature_extraction import DictVectorizer
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
#from nltk.parse import standford
import codecs
#import lemmatizing
##############################################################################
##############################################################################
##################### N-Gram Set in File HERE !!!!
##################### Visit :   http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
#####################           http://scikit-learn.org/stable/modules/feature_extraction.html
#####################           http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
#####################           http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html
##############################################################################
##############################################################################

class LemmaTokenizer(object):
    def __init__(self):
        self.wnl = WordNetLemmatizer()
    def __call__(self, articles):
        return [self.wnl.lemmatize(t) for t in word_tokenize(articles)]
# def vectorization(vectorizer, dataInput):
#     vector = vectorizer.fit_transform(dataInput)
#     return vector

def writeFile(nameFile, content):
    nameFile= 'Feature/'+nameFile
    #print (nameFile)
    fo = open(nameFile + '.txt', 'w', encoding="utf-8")
    print ('Feature : '+str(len(content)))
    for word in content:
        fo.write(word+'\n')
    fo.close

def nlktToken(dataInput,stopW):
    dicToken = []
    #fo = open('feature/Token_NLTK.txt', 'w')
    i=0
    for doc in dataInput.data:
        dicToken.append(str(word_tokenize(doc)))
        i= i+1
        print (i)
    writeFileName = 'Token_NLTK'
    writeContent = dicToken
    writeFile(writeFileName,writeContent)
    #return dicToken


def wordLemmatizer(dataInput):
    wordLemma = []
    lemmazer = WordNetLemmatizer()
    for word in dataInput:
        wordLem = lemmazer.lemmatize(word)
        #print (wordLem)
        wordLemma.append(wordLem)
    return wordLemma

def countVector(dataInput, stopW):
    if stopW is None:
        stopW = 'None'
    vectorizer = CountVectorizer(
        stop_words='english', tokenizer=LemmaTokenizer())
    # vectorization(vectorizer, dataInput)
    labels = dataInput.target #Mark Label to Doc
    #print (labels)
    print('Class : ' + str(list(dataInput.target_names)))
    vector = vectorizer.fit_transform(dataInput.data)    
    print('Size Matrix : '+str(vector.shape))
    print('**********************************************')
    

    #print (vector.todense())
    #print (vectorizer.vocabulary_)
    x= vectorizer.get_feature_names()
    #print (x)

    ######## write Feature 2 File.txt ######
    writeFileName = 'Token_Sp'
    writeContent = x
    writeFile(writeFileName,writeContent)
    ########################################
    #print('Token SP ==> OK')
    return vector


def dictVector(dataInput, stopW):
    
    vectorizer = DictVectorizer()
    # vectorization(vectorizer, dataInput)
    vector = vectorizer.fit_transform(dataInput)
    x= vectorizer.get_feature_names()
    writeFileName = 'Token_Di'
    writeContent = x
    writeFile(writeFileName,writeContent)
    #print (x)
    return vector


def hashVector(dataInput, stopW):
    if stopW is None:
        stopW = 'None'
    vectorizer = HashingVectorizer()
    # vectorization(vectorizer, dataInput)
    vector = vectorizer.fit_transform(dataInput)
    return vector

def tfidfVector(dataInput,stopW):
    if stopW is None:
        stopW = 'None'
    vectorizer = TfidfVectorizer(stop_words=stopW)

# def standford(dataInput,stopW):

