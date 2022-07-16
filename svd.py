import json
import numpy
from collections import Counter

filename = "search_spider/toy-data.json"

documents = [] # holds list of document urls, index corresponds to doc's col
words = [] # holds list of words, index corresponds to word's row

matrixArray = []

with open(filename, "r") as file:
    file_data = json.load(file)
    for document in file_data["data"]:
        documents.append(document["url"])
        worddict = Counter({})
        for string in document["texts"]:
            worddict = Counter(worddict) + Counter(string.split())
        worddict = dict(worddict)

        column = []

        for i in range(len(words)):
            if words[i] in worddict:
                column.append(worddict[words[i]])
                worddict.pop(words[i])
            else:
                column.append(0)
            i += 1

        for uncaughtkey in worddict:
            words.append(uncaughtkey)
            column.append(words[uncaughtkey])
        
        matrixArray.append(column)

print(matrixArray)

    
    
