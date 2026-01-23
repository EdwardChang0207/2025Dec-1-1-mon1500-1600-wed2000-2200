k = int(input())
x1, y1 = input().split()
x1, y1 = int(x1), int(y1)
x2, y2 = input().split()
x2, y2 = int(x2), int(y2)
p = 0
#重複
while k > 0:
    #一回合
    p += k
    #條件
    if p % x1 == 0: k -= y1
    if p % x2 == 0: k -= y2
print(p)