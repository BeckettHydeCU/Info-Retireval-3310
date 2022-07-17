from __future__ import print_function
import json
import numpy as np

#nltk imports
import nltk
nltk.data.path.append("/home/gigabyte/Desktop/matrixMethods/project/Info-Retireval-3310/nltk")
nltk.data.path.append("/home/becketth/3310/Info-Retireval-3310/nltk")
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk.stem as stem

from collections import Counter

filename = "search_spider/text-data.json"

stopWords = set(stopwords.words('english'))

stemmer = stem.PorterStemmer()

documents = [] # holds list of document urls, index corresponds to doc's col
words = [] # holds list of words, index corresponds to word's row

matrixArray = []

with open(filename, "r") as file:
    file_data = json.load(file)
    for document in file_data["data"]:
        documents.append(document["url"])

        doc_words = {}

        doc_raw = word_tokenize(" ".join(document["texts"]).lower())
        for w in doc_raw:
            w = stemmer.stem(w)
            if w not in stopWords:
                if w not in doc_words:
                    if w.isalpha()==True:
                        doc_words[w] = 1
                else:
                    doc_words[w] += 1

        # print(doc_words)

        column = []

        for i in range(len(words)):
            if words[i] in doc_words:
                column.append(doc_words[words[i]])
                doc_words.pop(words[i])
            else:
                column.append(0)
            i += 1

        for uncaughtkey in doc_words:
            words.append(uncaughtkey)
            column.append(doc_words[uncaughtkey])
        
        norm = np.linalg.norm(column, ord=2)
        normed_col = []
        for c in column:
            if norm == 0:
                normed_col.append(0)
            else:
                normed_col.append(c/norm)

        
        matrixArray.append(normed_col)
# print(matrixArray)

np.savetxt("documents.txt", documents, delimiter =", ", fmt ="% s")
np.savetxt("words.txt", words, delimiter=", ", fmt="% s")

for doc in matrixArray:
    d = (len(words) - len(doc))
    if (d > 0):
        for i in range(d):
            doc.append(0)

# print(matrixArray)

print("+++++++++==")
M = np.transpose(np.array(matrixArray))

print(M)

np.savetxt('pre-svd.txt', M)


# M1 = np.loadtxt('m.txt', dtype=int)

# print(M1)

    
    
