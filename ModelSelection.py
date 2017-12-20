from sklearn.model_selection import cross_val_score, cross_validate
from sklearn.metrics import recall_score
from sklearn.metrics.scorer import make_scorer
import modeling


k = 5


def cv(dataInput, classifier, k):
    scores = cross_val_score(classifier
                            , dataInput.data
                            , dataInput.target
                            , cv=k)
    return scores

def cvMultiEva(dataInput, classifier, k):
    scoring = {'prec_macro': 'precision_macro',
                'rec_micro': make_scorer(recall_score, average='macro')}
    scores = cross_validate(classifier 
                            , dataInput.data
                            , dataInput.target
                            , scoring=scoring
                            , cv = k
                            , return_train_score=True
                            )
    return scores