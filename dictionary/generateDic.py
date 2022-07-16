import nltk

#nltk imports
nltk.data.path.append("/home/gigabyte/Desktop/matrixMethods/project/Info-Retireval-3310/nltk")
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
 

#https://pythonspot.com/nltk-stop-words/
data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
stopWords = set(stopwords.words('english'))
words = word_tokenize(data)
wordsFiltered = []
for w in words:
    if w not in stopWords and w not in wordsFiltered:
        if w.isalpha()==True:
            wordsFiltered.append(w)

print(wordsFiltered)