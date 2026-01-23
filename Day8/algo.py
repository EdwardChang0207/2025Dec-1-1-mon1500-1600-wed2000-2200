'''
演算法：解決特定問題的方法
Input, Output, 明確性, 有限性, 有效性

(1)搜尋 Search: 
    1.Linear Search [],[],[],[],[],...,[] n -> max:n 
    2.Binary Search 0~100 100 -> max:lgn
(2)排序 Sort: 
    1.初級: 
        Bubble Sort -> n^2
        [5 4] 3 2 1
        R1: 
            1.4 [5 3] 2 1
            2.4 3 [5 2] 1  
            3.4 3 2 [5 1]
            4.[4 3] 2 1 5
        R2:
            1.3 [4 2] 1 5
            2.3 2 [4 1] 5
            3.[3 2] 1 4 5
        R3:
            1.2 [3 1] 4 5
            2.[2 1] 3 4 5
        R4:
            1.1 2 3 4 5

        5 items -> 4R, 10steps
        10items -> 9R, 45steps
        n items -> (n-1)R, n(n-1)/2=n^2 step
    
    Insertion Sort, Selection Sort
    2.高級: Quick Sort, Merge Sort
    3.線性: Bucket Sort, Radix Sort
'''
import random
l = [random.randint(1, 10) for i in range(10)]

def Linear_Search(l, target):
    print(l)
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

print(Linear_Search(l, 3))

def Binary_Search(l, target):
    upper = len(l)-1
    lower = 0
    while upper > lower:
        mid = (upper+lower)//2
        if l[mid] == target: return mid
        elif l[mid] > target: upper = mid-1
        else: lower = mid+1
    return -1

l = [i for i in range(10)]
print(Binary_Search(l, 3))