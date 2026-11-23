from collections import Counter

def matchingStrings(stringList, queries):
    freq = Counter(stringList)
    return [freq[q] for q in queries]
