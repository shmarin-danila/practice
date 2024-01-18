import random
A = []
for i in range(5):
    B = []
    for i in range(5):
        B.append(random.randint(-10, 10))
    A.append(B)
for i in A:
    for i1 in i:
        print(i1, end=' ')
    print()
sum = 0
count = 0
for i in range(5):
    for i1 in range(i + 1, 5):
        if A[i][i1] > 0:
            sum += A[i][i1]
            count += 1

print("a", sum)
print("b", count)
