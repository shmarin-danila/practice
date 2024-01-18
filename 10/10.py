import random
A = []
for i in range(5):
    B = []
    for i in range(5):
        B.append(random.randint(-9, 9))
    A.append(B)

with open('C:\\Users\\79304\\Desktop\\10pr\\Shmarin_UB-32_vvod.txt', 'w') as vvod:
    for i in A:
        vvod.write(' '.join([str(a) for a in i]) + '\n')
with open('C:\\Users\\79304\\Desktop\\10pr\\Shmarin_UB-32_vivod.txt', 'w') as vivod:
    sum = 0
    count = 0
    for i in range(5):
        for i1 in range(i + 1, 5):
            if A[i][i1] > 0:
                sum += A[i][1]
                count += 1
    vivod.write("Summa")
    vivod.write(' ')
    vivod.write(str(sum))
    vivod.write('\n')
    vivod.write("count")
    vivod.write(' ')
    vivod.write(str(count))
