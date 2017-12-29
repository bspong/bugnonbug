#from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
#from nltk.tokenize import word_tokenize
#import codecs
import time
import loadData



pathTrain = 'DataSet/train'
pathTest = 'DataSet/test_'

train_data = []
train_labels = []
test_data = []
test_labels = []
conTrain = loadData.loadData(pathTrain)
conTest = loadData.loadData(pathTest)
print('TrainSet : ' + str(len(conTrain.data)) + ' Report')
print('TrainSet : ' + str(len(conTest.data)) + ' Report')


vectorizer = TfidfVectorizer (min_df = 10,
                                max_df=1.0,
                                use_idf=True)

train_vectors = vectorizer.fit_transform(conTrain)
train_labels = conTrain.target
test_vectors = vectorizer.transform(conTest)
test_labels = conTest.target


clf = BernoulliNB()
t0 = time.time()
clf.fit(train_vectors, train_labels)
t1 = time.time()

prediction = clf.predict(test_vectors)
t2 = time.time()
time_train = t1-t0
time_Predict = t2-t1



print ('Train Time :'+ time_train)
print('Train Prediction :' + time_Predict)
