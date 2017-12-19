#from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold


kf = KFold(n_splits=2)
for train, test in kf.split(X):
    print ()