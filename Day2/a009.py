s = input()
# ord() #str -> ascii
# chr() #ascii -> str

for i in s:
    c = ord(i)
    r = chr(c-7)
    print(r, end='')