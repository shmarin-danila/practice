a = []
s = 0
for i in range(10) :
    a.append(int(input()))
for i in range(10):
    if a[i] > 5 :
        s += a[i]
print(s)
