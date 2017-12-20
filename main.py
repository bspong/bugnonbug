import readFile
import preProcess
#import loadDataScikit
from sklearn.feature_extraction.text import CountVectorizer
import loadData
import tokenVec
import weighting
import ModelSelection
#import bm25_

#from sklearn.feature_extraction import DictVextorzier

#bugContent = []

# pathFile = 'DataSet/Bug/'
pathFile = 'DataSet'
stopWord = 'english'
# #readFile.ReadAllinDir(pathFile)
# # bugContent = readFile.ReadAllinDir(pathFile)
# bugContent = loadDataScikit.loadDataSet(pathFile)
# print (len(bugContent.data))
# #print (bugContent)
# contentClear = preProcess.generalTokeni(bugContent)
# # print (contentClear)

# # Text preprocessing, 
# # tokenizing and filtering of stopawords are included 
# # in a high level component that is able to build 
# # a dictionary of features and transform documents 
# # to feature vector
# scount_vect = CountVectorizer() 
# #training = count_vect.fit()
print ('######################################################')
contentVec = loadData.loadData(pathFile)
print('DataSet : ' + str(len(contentVec.data)) + ' Report')
# x = contentVec.toarray()
# print (x)

#print('#####################2################################')

vecContent = tokenVec.countVector(contentVec,stopWord)
#bm25_.BM25Score(vecContent)

vecWeighted = weighting.tf_idf_Weigth(vecContent)
#ModelSelection.cv(vecWeighted, classifier, 5)
# x = vecWeighted.toarray()
# print(x)
# x = []
# X = tokenVec.countVector(train_dataSet).get_feature_name()
# print (x)
