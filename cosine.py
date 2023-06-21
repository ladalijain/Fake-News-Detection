import math
import re
import nltk
nltk.download('wordnet')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def tokenize(text):
    """Converts a text string into a list of tokens (words)."""
    text = text.lower()
    tokens = re.findall(r'\b\w+\b', text)
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return set(tokens)


def detectFakeWithCosine(text1, text2, threshold):
    tokens1 = tokenize(text1)
    tokens2 = tokenize(text2)

    # Create a set of all unique words in both texts
    all_words = tokens1.union(tokens2)

    # Create vectors of word frequencies for each text
    vector1 = [list(tokens1).count(word) for word in all_words]
    vector2 = [list(tokens2).count(word) for word in all_words]

    # Calculate the dot product and magnitudes of the vectors
    dot_product = sum([vector1[i] * vector2[i] for i in range(len(vector1))])
    magnitude1 = math.sqrt(sum([count**2 for count in vector1]))
    magnitude2 = math.sqrt(sum([count**2 for count in vector2]))
    cosine_similarity = dot_product / (magnitude1 * magnitude2)
    return round(cosine_similarity, 3)
    '''
    if cosine_similarity >= float(threshold):
        return "Real"
    else:
        return "Fake"
    '''


