from sklearn.datasets import load_files
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.feature_extraction.text import TFidfVectorizer
from nltk.tokenize import word_tokenize
#from sklearn.feature_extraction import DictVectorizer
#from sklearn.naive_bayes import MultinomialNB
import codecs


def setLoadData(pathFile):
    #res = load_files(pathFile)
    Category = ['bug', 'invalid']
    res = load_files(pathFile                     # , categories='Category'
                     #, encoding='utf-8'
                     #, encoding='latin-1'
                     , description=None, categories=None
                     , load_content=True, shuffle=True
                     , encoding='latin-1'
                     , decode_error='strict'
                     , random_state=0
                     )
    return (res)

def loadData (pathFile):
    trainSubset = setLoadData(pathFile)
    numFeature = len(trainSubset.data)
    return (trainSubset)
