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
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer 
#from sklearn.feature_extraction.text import TFidfVectorizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction import DictVectorizer
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
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
                    #, random_state=0
                    )
    return (res)


#pathFile = 'datasetSmall'
pathTrain = 'DataSet/train'
pathTest = 'DataSet/test_'
text_train_subset = loadDataSet(pathTrain)
text_test_subset = loadDataSet(pathTest)
print (len(text_train_subset.data)) 
print("%d categories" % len(text_train_subset.target_names))
#labels = text_train_subset.target #Mark Label to Doc
#print (labels)


print(list(text_train_subset.target_names)) ## print label 

vectorizer = TfidfVectorizer(stop_words='english', use_idf=True)
fo = open ('TrainFeature.txt','w')
x = vectorizer.fit_transform(text_train_subset.data)

for word in vectorizer.get_feature_names():
    fo.write(word + '\n')
fo.close()


y = vectorizer.fit_transform(text_test_subset.data)
print('Train : '+str(x.shape))
print('Test : ' + str(y.shape))

# vectorizer = DictVectorizer()
# vectorizer.fit_transform(text_train_subset.data)
#vectorizerTFidf = TFidfVectorizer()

#text_test_subset = text_train_subset # load your actual test data here

# Turn the text documents into vectors of word frequencies 
vectorizer = TfidfVectorizer(stop_words='english', use_idf=True)
X_train = vectorizer.fit_transform(text_train_subset.data)
y_train = text_train_subset.target
#print (y_train)


classifier = BernoulliNB(alpha=0).fit(X_train, y_train)
print("Training score: {0:.1f}%".format(
    classifier.score(X_train, y_train) * 100))
print ('###########################################')


# Evaluate the classifier on the testing set
X_test = vectorizer.transform(text_test_subset.data)
y_test = text_test_subset.target

print("Testing score: {0:.1f}%".format(
    classifier.score(X_test, y_test) * 100))
