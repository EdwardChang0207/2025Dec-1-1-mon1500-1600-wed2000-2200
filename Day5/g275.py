n = int(input())
for i in range(n):
    w = input().split()
    m = input().split()
    r = ''
    if w[1] == w[3] or w[1] != w[5] or m[1] == m[3] or m[1] != m[5]:
        r += 'A'
    if w[6] != '1' or m[6] != '0':
        r += 'B'
    if w[1] == m[1] or w[3] == m[3] or w[5] == m[5]:
        r += 'C'
    if r:
        print(r)
    else:
        print('None')