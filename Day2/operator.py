# 運算子 Operator
'''
1.數學運算子 num op num -> num
    +, -, *, /, **(指數), //(整數除法、商數), %(餘數)
    print(2**3)
    print(20//3)
    print(20%3)
    print(4**.5)
    print(4 % 2)
    ['a','b','c','d','e']
    # 0.  1.  2.  3.  4 -> i
    # 1.  2.  3.  1.  2 -> (i+1)%3
2.邏輯運算子 num op num -> bool
    <,>,==,!=,<=,>=,in

    print(3 >= 1)

    l = [1, 2, 3]
    print(4 in l)  
3.布林運算子 bool op bool -> bool
    not, or, and, xor
    (1)not 反閘
        周杰倫：哎呦不錯喔 -> True
        不(not)錯(False) -> True
        錯  -> False
        不(not)行(True) -> False
        行  -> True
        
        ex.
            print(not True)
            print(not False)
    (2)or 或閘
        兩件事至少發生一件
        math or english -> 3000
        T       F           T
        F       T           T
        T       T           T
        F       F           F

        ex.
            a = False
            b = False
            print(a or b)
    (3)and 且閘
        兩件事，兩件都要發生
        hw and 打掃 -> :)
        T       F       F
        F       T       F
        T       T       T
        F       F       F

        ex.
            a, b = False, False
            print(a and b)
    (4)xor (excursive or)
        兩件是只發生其中一件
        珍奶 xor 烏龍 -> :)
        T       F       T
        F       T       T
        T       T       F
        F       F       F
        [1] not, or, and
            (a or b) and not(a and b)

            ex.
                a, b = False, False           
                print((a or b) and not(a and b))
        [2] binary
            ex.
                a, b = False, False
                print(a^b)
        # print(1 xor 3)
        a = 1
        b = 3
        print((a or b) and not(a and b))
        print(a^b)

#string & list
(1)+
    print('abc'+'efg')
    print([1,2,3]+[4,5,6])
(2)*
    print('abc'*3)
    print([123]*3)
l = [1, 2, 3]
print(l[2])
s = 'abc'
print(s[2])
print('a' in s)

>= -> > or ==
'''
a = 1
a = a + 1# a += 1