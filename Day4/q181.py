a, b = [int(i) for i in input().split()]
n = int(input())
t = [int(i) for i in input().split()]
r = 0

for i in t:
    if i % (a + b) >= a:
       r += (a + b) - i % (a + b)

print(r)