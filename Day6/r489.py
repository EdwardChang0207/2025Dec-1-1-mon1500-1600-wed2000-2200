R, C = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()] for j in range(R)]
B = [[int(i) for i in input().split()] for j in range(R)]

best = 0

for k in range(4):
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        r = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == B[i][j]: r += 1
        cur = r//(R*C)*100
        if cur > best: best = cur

    #rotate
    B.reverse()
    BT = []
    for i in range(len(B[0])):
        col = []
        for j in range(len(B)):
            col.append(B[j][i])
        BT.append(col)
    B = BT

print(f'{best}%')
# print(best,'%',sep='')