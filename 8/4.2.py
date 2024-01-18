import random
N = 5
A = []
for i in range(N):
    B = []
    for i in range(N):
        B.append(random.randint(-10, 10))
    A.append(B)
print("matrica")
for i in A:
    for elem in i:
        print(elem, end=' ')
    print()
print()
for i in range(N):
    for j in range(N):
        if A[i][j] > 0:
            A[i][j] = 1
        else:
            A[i][j] = 0
print("0 ili 1")
for i in A:
    for elem in i:
        print(elem, end=' ')
    print()
print("treugol")
for i in range(len(A)):
    print(*[A[i][j] if j <= i else ' ' for j in range(len(A[i]))], ' ')
