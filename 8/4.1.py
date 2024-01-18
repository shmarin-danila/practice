import random
N = 7
A = []
for i in range(N):
    B = []
    for i in range(N):
        B.append(random.randint(0, 10))
    A.append(B)
print("matrica")
for i in A:
    for elem in i:
        print(elem, end=' ')
    print()
print()
s = []
for i in A:
    s.append(sum(i))
for i in range(N):
    if sum(A[i]) == max(s):
        print(A[i], max(s))
for i in range(N):
    if sum(A[i]) == min(s):
        print(A[i], min(s))
