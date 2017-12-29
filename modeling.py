from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB

acc = 0

# def classification(clf):
#     clf.fit(X_train, y_train)
def gNB (xTrain, yTrain, xTest, yTest):
    classifier = GaussianNB().fit(xTrain, yTrain)
    acc = classifier.score(xTest, yTest)*100
    return acc

def bNB (x_Train, y_Train, xTest, yTest):
    classifier = BernoulliNB().fit(x_Train, y_Train)
    acc = classifier.score(x_Train, y_Train) * 100
    print ('ACC{0:.01f}%'.format(acc))
    #return acc

def mNB (xTrain, yTrain, xTest, yTest):
    classifier = MultinomialNB().fit(xTrain, yTrain)
    acc = classifier.score(xTest, yTest)*100
    return acc
