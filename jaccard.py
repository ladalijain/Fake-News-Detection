import re
import math

def tokenize(text):
    """Converts a text string into a list of tokens (words)."""
    text = text.lower()
    tokens = re.findall(r'\b\w+\b', text)
    return set(tokens)

def detectFakeWithJaccard(text1, text2, threshold):
    tokens1 = tokenize(text1)
    tokens2 = tokenize(text2)
    intersection = tokens1.intersection(tokens2)
    union = tokens1.union(tokens2)
    sim = len(intersection) / len(union)
    return round(sim, 3)


    # if sim >= float(threshold):
    #     return "Real"
    # else:
    #     return "Fake"