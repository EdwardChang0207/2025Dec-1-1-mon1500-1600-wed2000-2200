l = input().split()

M=int(l[0])
D=int(l[1])
S=(M*2+D)%3

luck = ['普通','吉','大吉']
#.       0.     1.   2
print(luck[S])