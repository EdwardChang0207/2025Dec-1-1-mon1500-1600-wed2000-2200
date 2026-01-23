n = int(input())
s = [int(i) for i in input().split()]

s.sort()
print(*s)# * -> for all: print(s[0],s[1],s[2],...)

if s[-1] < 60:
    print(s[-1])
    print('worst case')

elif s[0] >= 60:
    print('best case')
    print(s[0])

else:#... a | b
    for i in range(len(s)):
        if s[i] >= 60:
            print(s[i-1])
            print(s[i])
            break