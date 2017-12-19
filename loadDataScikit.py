# import os
# import shutil
# import tempfile
# #import sklearn.datasets as sk
# from sklearn.datasets import load_files
# # pathFile = '..\DataSet\\'
# # sk.load_files(pathFile,description=None, categories=None, load_content=True, shuffle=True, encoding=utf-8, decode_error=’strict’, random_state=0)
# LOAD_FILES_ROOT = '/DataSet'
# res = []
# res = load_files(LOAD_FILES_ROOT, encoding="utf-8")


from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer 
#from sklearn.feature_extraction.text import TFidfVectorizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction import DictVectorizer
from sklearn.naive_bayes import MultinomialNB
import codecs


def loadDataSet (pathFile):
    #res = load_files(pathFile)
    Category = ['bug', 'invalid']
    res = load_files(pathFile
                    # , categories='Category'
                    #, encoding='utf-8'
                    #, encoding='latin-1'

                    , description=None
                    , categories=None
                    , load_content=True
                    , shuffle=True
                    , encoding='latin-1'
                    , decode_error='strict'
                    , random_state=0
                    )
    return (res)

pathFile = 'DataSet'
text_train_subset = loadDataSet(pathFile)
print (len(text_train_subset.data)) 
print("%d categories" % len(text_train_subset.target_names))
#labels = text_train_subset.target #Mark Label to Doc
#print (labels)


print('\n\n')
print(list(text_train_subset.target_names))

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(text_train_subset.data)
print(x.shape)




# vectorizer = DictVectorizer()
# vectorizer.fit_transform(text_train_subset.data)
#vectorizerTFidf = TFidfVectorizer()



text_test_subset = text_train_subset # load your actual test data here

# Turn the text documents into vectors of word frequencies
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(text_train_subset.data)
y_train = text_train_subset.target


classifier = MultinomialNB().fit(X_train, y_train)
print("Training score: {0:.1f}%".format(
    classifier.score(X_train, y_train) * 100))

# Evaluate the classifier on the testing set
X_test = vectorizer.transform(text_test_subset.data)
y_test = text_test_subset.target
print("Testing score: {0:.1f}%".format(
    classifier.score(X_test, y_test) * 100))
