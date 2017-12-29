import numpy as np

def gobalWeight():
    print ('')


def localWeight(vecInput):
    print(vecInput.shape[0])

def findLen(vecInput):
    docLen = []
    corfreq = 0
    wFreq = 0
    for doc in vecInput[0:]:
        wFreq = doc.sum()
        corfreq = corfreq + wFreq          
        docLen.append(wFreq)
    avgDocLen = corfreq / vecInput.shape[0]
    # print (avgDocLen)
    print (docLen)
    # print (i)
    # print(len(docLen))
    return docLen, avgDocLen
def findIDF():
    docIDF[] = math.log((self.N - self.DF[term] + 0.5) / (self.DF[term] + 0.5), base)
    return docIDF

def BM25Score(vecInput):
    scores = []
    k1 = 1.2
    pri
    b = 0.5
    doclen, avgCorFreq = findLen(vecInput)
    print(doclen[2])
    docLen = vecInput.shape[0]
    pri
    #fo = open('test.txt', 'w')
    #i=0
    doc = vecInput.toarray()
    print(vecInput.shape[1])
    #print (type(vecInput))
    print('*************************************************************')
    for x_row in range(len(doc)):
        tmp_score = []
        for y_col in range(len(doc[0])):
            print(doc[x_row][y_col])
            upper = (doc[x_row][y_col] * (k1 + 1))
            below = (doc[x_row][y_col] + k1 *
                     (1 - b + b * docLen[x_row] / avgCorFreq))
            tmp_score.append(IDF[x_row][y_col]*upper/below)
        scores.append(sum(tmp_score))
            #print (word)
        #i=i+1
        # print(i)
    #fo.close()
    #findLen(vecInput)
    #localWeight(vecInput)
