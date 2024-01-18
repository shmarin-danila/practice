k1=0
def sum1(b):
    global k1
    if (b == 0):
        return k1
    k = b % 10
    k1 += k
    sum1(b // 10)
n = int(input())
sum1(n)
print(k1)
