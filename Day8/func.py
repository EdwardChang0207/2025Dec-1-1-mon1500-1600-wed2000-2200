#top-down
R, C = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()] for j in range(R)]
B = [[int(i) for i in input().split()] for j in range(R)]
r = 0
def compare(A, B):
    r = 0
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == B[i][j]: r += 1
    r //= (len(A)*len(A[0]))
    r *= 100
    return r

def rotate(M:list):
    M.reverse()
    MT = []
    for i in range(len(M[0])):
        col = []
        for j in range(len(M)):
            col.append(M[j][i])
        MT.append(col)
    return MT

for i in range(4):
    r = max(r, compare(A, B))
    B = rotate(B)
print(r)