from sklearn.feature_extraction import DictVectorizer, FeatureHasher
from collections import defaultdict
import re

from sklearn.datasets import fetch_20newsgroups


def tokens(doc):
    """Extract tokens from doc.

    This uses a simple regex to break strings into tokens. For a more
    principled approach, see CountVectorizer or TfidfVectorizer.
    """
    return (tok.lower() for tok in re.findall(r"\w+", doc))

def token_freqs(doc):
    """Extract a dict mapping tokens from doc to their frequencies."""
    freq = defaultdict(int)
    for tok in tokens(doc):
        freq[tok] += 1
    return freq

def dictTonken(raw_data):
    vectorizer = DictVectorizer()
    # for d in raw_data:
    #     vectorizer.fit_transform(token_freqs(d))
    vectorizer.fit_transform(token_freqs(d) for d in raw_data)
    print (vectorizer.vocabulary_)
    #print (vectorizer.get_feature_names)

# categories = [
#     'alt.atheism',
#     'comp.graphics',
#     'comp.sys.ibm.pc.hardware',
#     'misc.forsale',
#     'rec.autos',
#     'sci.space',
#     'talk.religion.misc',
# ]

# raw_data = fetch_20newsgroups(subset='train', categories=categories).data
# #dictTonken(raw_data)
# print (raw_dat