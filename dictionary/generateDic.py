import nltk
import json
import numpy

#nltk imports
nltk.data.path.append("/home/gigabyte/Desktop/matrixMethods/project/Info-Retireval-3310/nltk")
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

#ntlk setup
#https://pythonspot.com/nltk-stop-words/
stopWords = set(stopwords.words('english'))

#get the data and create dictionary
filename = "text-data-mfwebsite.json"
wordsFiltered = [] #holds the list of terms for document matrix

with open(filename, "r") as file:
    file_data = json.load(file)
    for document in file_data["data"]:
        #print(" ".join(document["texts"]))
        words = word_tokenize(" ".join(document["texts"]))
        for w in words:
            if w not in stopWords and w not in wordsFiltered:
                if w.isalpha()==True:
                    wordsFiltered.append(w)
                    
print(wordsFiltered)

       


# data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
# stopWords = set(stopwords.words('english'))
# words = word_tokenize(data)
# print(type(words))
# wordsFiltered = []
# for w in words:
#     if w not in stopWords and w not in wordsFiltered:
#         if w.isalpha()==True:
#             wordsFiltered.append(w)

# print(wordsFiltered)