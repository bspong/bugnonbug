from sklearn.feature_extraction.text import TfidfTransformer

def tf_idf_Weigth(vector):
    transformer = TfidfTransformer()
    vecWeigthed = transformer.fit_transform(vector)

    #arrayWeighted = vecWeigthed.toarray()
    #print(arrayWeighted)
    
    return vecWeigthed#, arrayWeighted

