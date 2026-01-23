R, C, M = [int(i) for i in input().split()]
B = [input().split() for j in range(R)]
mk = [int(i) for i in input().split()]
mk.reverse()
for i in mk:
    if i == 0:
        #rotate
        #T
        A = []
        for j in range(len(B[0])):
            row = []
            for k in range(len(B)):
                row.append(B[k][j])
            A.append(row)
        B = A
        #filp
        B.reverse()    
    else:
        #filp
        B.reverse()
print(len(B), len(B[0]))
for r in B:
    print(*r)