'''
variable -> 箱子
'''
# name = input()
# print('hello,', name)

'''
kevin -> kevin

kevin
18
-> my name is kevin, and I am 18 years old.
'''

# name = input()
# age = input()
# name, age = input(), input()
# print('my name is ',name,', and I am', age, 'years old.')

'''
格式化 format

格式符號
%s -> str
%d -> int
%f -> float

(1) %
(2) .format
(3) f-string (function)

XX 18
XXX 9
name, age = 'kevin', 18
name1, age1 = 'andy', 8
name2, age2 = 'cindy', 100

print('my name is %5s, and I am %3d years old.' % (name, age))
print('my name is {:5s}, and I am {:3d} years old.'.format(name1, age1)) #. (1)的 (2)對...做...
print(f'my name is {name2:5s}, and I am {age2:3d} years old.')
'''

print('%5.2f'%(3.14159))
print('{:.2f}'.format(3.14159))
print(f'{3.14159:.2f}')