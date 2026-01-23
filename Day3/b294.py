n = int(input())
amount = input().split()#['1','2','3',..]
cost = 0
for i in range(n):#0~n-1
    cost += (i+1)*int(amount[i])
print(cost)