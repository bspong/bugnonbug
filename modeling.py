from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB

gnb = GaussianNB()
bnb = BernoulliNB()
mnb = MultinomialNB()

def classification(clf):
    clf.fit(X_train, y_train)