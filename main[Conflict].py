import readFile
#import preProcess
#import loadDataScikit
#from sklearn.feature_extraction.text import CountVectorizer
import loadData
import tokenVec
import weighting
import modeling
#import ModelSelection
#import bm25_

#from sklearn.feature_extraction import DictVextorzier

#bugContent = []

# pathFile = 'DataSet/Bug/'
#pathFile = 'datasetSmall'
pathTrain = 'dataset/train'
pathTest = 'dataset/test_'
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
#contentVec = loadData.loadData(pathFile)
conTrain = loadData.loadData(pathTrain)
conTest = loadData.loadData(pathTest)
#print (contentVec.taget)
#print(type(contentVec))
print('TrainSet : ' + str(len(conTrain.data)) + ' Report')
print('TrainSet : ' + str(len(conTest.data)) + ' Report')
# x = contentVec.toarray()
# print (x)

#print('#####################2################################')

#vecContent = tokenVec.countVector(contentVec,stopWord)
vecTrain = tokenVec.countVector(conTrain,stopWord)
vecTest = tokenVec.countVector(conTest,stopWord)
print ('vecContent ==> OK')
#tokenVec.dictVector(contentVec, stopWord)
#tokenVec.nlktToken(contentVec,stopWord)
#print ('tokenVec ==> OK')
#bm25_.BM25Score(vecContent)

#vecWeighted = weighting.tf_idf_Weigth(vecContent)
vecWTrain = weighting.tf_idf_Weigth(vecTrain)
vecWTest = weighting.tf_idf_Weigth(vecTest)
print ('vecWeighted ==> OK')

#x_train = vecWeighted.data
#y_train = contentVec.target
#######################################
x_train = vecWTrain.data
y_train = conTrain.target

x_test = vecWTest.data
y_test = conTest.target
print (y_train)

modeling.bNB(x_train,y_train,x_test,y_test)


#ModelSelection.cv(vecWeighted, classifier, 5)
# x = vecWeighted.toarray()
# print(x)
# x = []
# X = tokenVec.countVector(train_dataSet).get_feature_name()
# print (x)
