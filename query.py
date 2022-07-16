import numpy as np

query1 = np.transpose([1, 0, 1, 0, 0, 0])
query2 = np.transpose([1, 0, 0, 0, 0, 0])

documents = np.loadtxt('documents.txt', dtype=str, delimiter="\n")
words = np.loadtxt('words.txt', dtype=str, delimiter="\n")

print(documents)
print(words)

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
    for i in range(len(words)):
        if words[i] in s:
            query.append(1)
        else:
            query.append(0)
    
    query = np.transpose(query)
    print(query)

    similarities = []

    for col in range(rankAppx.shape[1]):
        e = np.zeros(rankAppx.shape[1])
        e[col] = 1
        e = np.transpose([e])

        V = np.transpose(V_t)

        U_t = np.transpose(U)

        num = np.matmul(np.matmul(np.matmul(np.transpose(e), V), D), np.matmul(U_t, query))
        denom = np.linalg.norm(np.matmul(np.matmul(D, V_t), e), ord=2) * np.linalg.norm(query, ord=2)

        costheta = num/denom

        similarities.append(costheta[0])

    return similarities

print(query("bake"))
