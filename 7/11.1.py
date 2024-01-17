def prostoe(n):
    x = 2
    while n % x != 0:
        x += 1
    return x == n
n = int(input())
for i in range(n,2*n):
    if prostoe(i) == prostoe(i+2) == 1:
        print(i," ",i+2)
