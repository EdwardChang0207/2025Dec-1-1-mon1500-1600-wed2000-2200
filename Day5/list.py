'''
if ['']: print('hello')

l[start[init:0]:end[init:len(l)-1(-1)]:interval[init:1]]
l = [i for i in range(10)]
print(l[3::])

print(len(l))
max = l[0]
print(max(l))
print(min(l))
for i in range(len(l)):
    if l[i] > max: max = l[i]
print(sum(l))
s = 0
for i in range(len(l)):
    s += l[i]
l = [i for i in range(10)]
s = 1
for i in range(len(l)):
    s *= l[i]
print(s)

l = []
l.append(1)
l.append(2)
l.insert(0,3)
i = l.pop(0)
l.remove(1)
print(l, i)

l = [1,2,1,2,1,2,1,2,3]
l.remove(1)
print(l)

for i in range(len(l)):
    if l[i] == 1:
        l = l[:i]+l[i+1:]
        break
l = [1,2,3]
l.reverse()#3 2 1
l.sort()#1 2 3
l.reverse()# 3 2 1
print(sorted(l)) # 1 2 3
print(l) # 3 2 1

l = [1,2,3,1,2,3,1]
print(l.count(1))
print(l.index(3))

A = [[1,2,3],
     [4,5,6]]

print(A[0][1])


m, n(size)
...
...
...(m rows)
m, n = [int(i) for i in input().split()]
A = []
for i in range(m):
    row = [int(i) for i in input().split()]
    A.append(row)

print(*A, sep='\n') #print(A[0], A[1], ...)

1.原本行(直)->列（橫）
2.原本列->行
'''
m, n = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()] for j in range(m)]
AT = []

for i in range(n): #收集一個col
    col = []

    for j in range(m):#收集col的一個element
        col.append(A[j][i])

    AT.append(col)

print(*AT, sep='\n')#print(AT[0], AT[1], ..., AT[n])