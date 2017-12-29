from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Assume thats the data we have (4 short documents)
data = [
    'I like beer and pizza',
    'I love pizza and pasta',
    'I prefer wine over beer',
    'Thou shalt not pass'
]

# Vectorise the data
vec = TfidfVectorizer()
X = vec.fit_transform(data) # `X` will now be a TF-IDF representation of the data, the first row of `X` corresponds to the first sentence in `data`

# Calculate the pairwise cosine similarities (depending on the amount of data that you are going to have this could take a while)
S = cosine_similarity(X)