n = int(input("Chislo: "))

summ = 0
fact = 1

for i in range(1, n + 1):
    fact = fact * i
    summ += fact
print(summ)
