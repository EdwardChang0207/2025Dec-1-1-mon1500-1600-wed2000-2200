n = int(input())
for i in range(n):
    l1 = input().split()
    l2 = input().split()
    r = ''
    #A
    for l in [l1,l2]:
        if l[1] == l[3] or l[1] != l[5]:
            r += 'A'
            break
    #B
    if l1[-1] == '0' or l2[-1] == 1:
        r += 'B'

    #C
    for j in range(1, 6, 2):
        if l1[j] == l2[j]:
            r += 'C'
            break
    
    if r: print(r)
    else: print('None')