from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfVectorizer
from sklearn.feature_extraction import DictVectorizer
import codecs
##############################################################################
##############################################################################
##################### N-Gram Set in File HERE !!!!
##################### Visit :   http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
#####################           http://scikit-learn.org/stable/modules/feature_extraction.html
#####################           http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
#####################           http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html
##############################################################################
##############################################################################


# def vectorization(vectorizer, dataInput):
#     vector = vectorizer.fit_transform(dataInput)
#     return vector

def writeFile(nameFile, content):
    fo = open(nameFile+'.txt','w')
    fo.write(content)
    fo.close


def countVector(dataInput, stopW):
    if stopW is None:
        stopW = 'None'
    vectorizer = CountVectorizer()
    # vectorization(vectorizer, dataInput)
    labels = dataInput.target #Mark Label to Doc
    #print (labels)
    print('Class : ' + str(list(dataInput.target_names)))
    vector = vectorizer.fit_transform(dataInput.data)    
    print('Size Matrix : '+str(vector.shape))
    print('**********************************************')
    
    ######## write Feature 2 File.txt ######
    # writeFileName = 'Token_Sp'
    # writeContent = vector.get_feature_names()
    # writeFile(writeFileName,writeContent)
    ########################################
  
    #print(x)
    #x = vectorizer.toarry()
    #print(x)
    return vector


def dictVector(dataInput, stopW):
    if stopW is None:
        stopW = 'None'
    vectorizer = DictVectorizer()
    # vectorization(vectorizer, dataInput)
    vector = vectorizer.fit_transform(dataInput)
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

