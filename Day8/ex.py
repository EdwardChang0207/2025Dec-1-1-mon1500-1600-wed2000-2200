def plus(a, b):
    return a+b

def matrix_plus(A:list, B:list):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] += B[i][j]
    return A

input()