from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer
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


def countVector (dataInput):
    vectorizer = CountVectorizer()
    # vectorization(vectorizer, dataInput)
    labels = dataInput.target #Mark Label to Doc
    #print (labels)
    print('Class : ' + str(list(dataInput.target_names)))
    vector = vectorizer.fit_transform(dataInput.data)
    print('Size Matrix : '+str(vector.shape))
    print('**********************************************')
    #print(vector.get_feature_names())
    return vector


def dictVector(dataInput):
    vectorizer = DictVectorizer()
    # vectorization(vectorizer, dataInput)
    vector = vectorizer.fit_transform(dataInput)
    return vector


def hashVector(dataInput):
    vectorizer = HashingVectorizer()
    # vectorization(vectorizer, dataInput)
    vector = vectorizer.fit_transform(dataInput)
    return vector



