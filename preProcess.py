from nltk.tokenize import word_tokenize
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
def lowChar(txtContent):
    all_words = []
    for w in txtContent:
        all_words.append(w.lower())
    return all_words

def generalTokeni(fileContent):
    contentTokened = []
    for contentList in fileContent:
        contentTokened.append(contentList.split())
    return contentTokened

def dictTansform():
    vectorizer = DictVectorizer()
    #vectorizer.fit_transform(token_freqs(d) for d in raw_data)

def hashingVectorizer(corpus,nFeatures):
    if nFeatures is None:
        nFeatures = 10
    hv = HashingVectorizer(nFeatures)
    contentVec = hv.transform(corpus)
    return contentVec


