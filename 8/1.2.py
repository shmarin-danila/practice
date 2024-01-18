import random
N = 5
M = 5
B = []
for i in range(N):
    A = []
    for i in range(M):
        A.append(random.randint(-10, 10))
    B.append(A)
print("nachalo")
for i in B:
    for i1 in i:
        print(i1, end=' ')
    print()
for i in range(N):
    max1 = max(B[i])
    min1 = min(B[i])
    maxi = B[i].index(max1)
    mini = B[i].index(min1)
    B[i][0] = B[i][maxi]
    B[i][maxi] = B[i][0]
    B[i][-1] = B[i][mini]
    B[i][mini] = B[i][-1]
print("konec")
for i in B:
    for i1 in i:
        print(i1, end=' ')
    print()
