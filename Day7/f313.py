R,C,k,m = [int(i) for i in input().split()]
P = [[int(i) for i in input().split()] for j in range(R)]
d = [[-1, 0],[1, 0],[0, -1],[0, 1]]

for _ in range(m):
    A = [[0]*C for i in range(R)]
    # A[i][j] -> A[i-1][j] A[i+1][j] A[i][j-1] A[i][j+1]
    for i in range(R):
        for j in range(C):
            if A[i][j] == -1: continue
            p = A[i][j] // k
            for x, y in d:
                if (i+x in range(0, R)) and (j+y in range(0, C)) and A[i+x][j+y] != -1:
                    A[i][j] -= p
                    A[i+x][j+y] += p
            
    for i in range(R):
        for j in range(C):
            P[i][j] += A[i][j]

M, m = A[0][0], A[0][0]
for i in range(R):
    for j in range(C):
        if A[i][j] == -1: continue
        elif A[i][j] > M: M = A[i][j]
        elif A[i][j] < m: m = A[i][j]
print(m)
print(M)