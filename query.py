import numpy as np

import nltk.stem as stem

stemmer = stem.PorterStemmer()

query1 = np.transpose([1, 0, 1, 0, 0, 0])
query2 = np.transpose([1, 0, 0, 0, 0, 0])

documents = np.loadtxt('documents.txt', dtype=str)
words = np.loadtxt('words.txt', dtype=str)

# print(documents)
# print(words)

qtext1 = "bake bread"
qtext2 = "bake"
    


U = np.loadtxt('U-appx.txt')
D = np.loadtxt('D-appx.txt')
V_t = np.loadtxt('Vt-appx.txt')

rankAppx = np.loadtxt('rank-appx.txt')

# def slowquery(query):

#     similarities = []

#     for col in range(rankAppx.shape[1]):
        

#         e = np.zeros(rankAppx.shape[1])
#         e[col] = 1
#         e = np.transpose([e])

#         abye = np.matmul(rankAppx, e)
#         num = np.matmul(np.transpose(abye), query)
#         denom = np.linalg.norm(abye, ord=2) * np.linalg.norm(query, ord=2)
        
#         costheta = num / denom

#         similarities.append(costheta[0])


#     return similarities


def query(querytext):

    query = []

    s = querytext.split()
    stemmed = []
    for ss in s:
        stemmed.append(stemmer.stem(ss.lower()))

    # print(stemmed)

    for i in range(len(words)):
        if words[i] in stemmed:
            query.append(1)
        else:
            query.append(0)
    
    query = np.transpose(query)
    # query = np.transpose([1,0,1,0,0,0])
    # print(query)

    similarities = []

    for col in range(rankAppx.shape[1]):
        e = np.zeros(rankAppx.shape[1])
        e[col] = 1
        e = np.transpose([e])

        V = np.transpose(V_t)

        U_t = np.transpose(U)

        num = np.matmul(np.matmul(np.matmul(np.transpose(e), V), D), np.matmul(U_t, query))
        denom = np.linalg.norm(np.matmul(np.matmul(D, V_t), e), ord=2) * np.linalg.norm(query, ord=2)

        if denom == 0:
            costheta = [-1]
        else:
            costheta = num/denom

        similarities.append(costheta[0])

    return similarities

resp = query("washington post published article innovator musician castle of our skins")

results = []
i = 0
for res in resp:
    if res > .1:
        results.append((res, documents[i]))
    i += 1

results = sorted(results, key = lambda x: x[1])

for result in results:
    print(str(result[0]) + " :: " + str(result[1]))

np.savetxt("results.txt", results, delimiter=", ", fmt="% s")


