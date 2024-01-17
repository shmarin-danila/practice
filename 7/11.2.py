import random
arrA=[[25, 10, 7, 8,85], 
      [532, 34, 423, 44, 99], 
      [423, 423, 22, 344, 555], 
      [444, 233, 955, 324, 444], 
      [123, 123, 123, 123, 123]]
arrB=[[325, 10, 43, 423, 985],
      [312, 321, 33, 22, 1],
      [312, 321, 33, 22, 1],
      [312, 321, 33, 22, 1],
      [312, 321, 33, 22, 1]]
def maxm(m1):
    max=0
    for i in range(5):
        for k in range(5):
            if max < m1[i][k]:
                max=m1[i][k]
                a=i
                b=k
    return(max, a, b)
m1, a1, b1=maxm(arrA)
m2, a2, b2=maxm(arrB)
arrA[a1][b1]=m2
arrB[a2][b2]=m1
print(arrA)
