import numpy as np

query1 = np.transpose([1, 0, 1, 0, 0, 0])
query2 = np.transpose([1, 0, 0, 0, 0, 0])


U = np.loadtxt('U-appx.txt')
D = np.loadtxt('D-appx.txt')
V_t = np.loadtxt('Vt-appx.txt')

rankAppx = np.loadtxt('rank-appx.txt')

def query(query):

    similarities = []

    for col in range(rankAppx.shape[1]):
        

        e = np.zeros(rankAppx.shape[1])
        e[col] = 1
        e = np.transpose([e])

        abye = np.matmul(rankAppx, e)
        num = np.matmul(np.transpose(abye), query)
        denom = np.linalg.norm(abye, ord=2) * np.linalg.norm(query, ord=2)
        
        costheta = num / denom

        similarities.append(costheta)


    return similarities

print(query(query2))
