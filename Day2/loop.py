'''
for -> while? O
while -> for? O
for or while?
while <condiction:bool>

索引值 index -> i
i = 1
while i <= 10:
    print(i)
    i += 1 

for sushi in ['鮭魚','鮪魚','拉麵']:
    print(sushi)
    if sushi == '拉麵':
        print('拿')

for i in 'hello':
    print(i) 

# range(start[init:0], end, interval[init:1])
# start -> end-1, increase interval
# 10 -> 1
l = [1,2,3,4,5]
#    0 1 2 3 4
for i in range(5): #0->4
    print(l[i]) #l[0], l[1], l[2]...
while True:
    input('///')
    ...

a = 1
for i in range(3):#0, 1, 2
    a += 1
print(a)

# [0, 1, 2, 3, 4]
l = [i for i in range(5)]
print(l)

#[0, 4, 16, 36, 64]
l = [i**2 for i in range(0, 9, 2)]
print(l)

#[0, 4, 36, 64]
l = [i**2 for i in range(0, 9, 2) if i != 4]
print(l)

# '0 2 4' -> ['0','2','4']
a, b, c = [int(i) for i in input().split()]
print(a, b, c)

continue(skip), break(stop)
for i in range(10):
    if i % 3 == 0: continue
    if i == 8: break
    print(i)
'''