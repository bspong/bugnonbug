def splitDataSet (train_test_split, dataset, test_size):
    if test_size is None:
        test_size = 0.5
    docs_train, docs_test, y_train, y_test = train_test_split(
        dataset.data, dataset.target, test_size)
