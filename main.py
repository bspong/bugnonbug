import readFile
import preProcess
#import loadDataScikit
from sklearn.feature_extraction.text import CountVectorizer
import loadData
import tokenVec

#from sklearn.feature_extraction import DictVextorzier

#bugContent = []

# pathFile = 'DataSet/Bug/'
pathFile = 'DataSet'
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
print ('#####################1################################')
train_dataSet = loadData.loadData(pathFile)
print ('DataSet : '+str(len(train_dataSet.data)) + ' Report')

print('#####################2################################')
tokenVec.countVector(train_dataSet)
# x = []
# X = tokenVec.countVector(train_dataSet).get_feature_name()
# print (x)
