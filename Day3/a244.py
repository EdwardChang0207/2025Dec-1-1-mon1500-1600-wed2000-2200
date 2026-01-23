n = int(input())
for i in range(n):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    if a == 1: print(b+c)
    elif a == 2: print(b-c)
    elif a == 3: print(b*c)
    else: print(b//c)