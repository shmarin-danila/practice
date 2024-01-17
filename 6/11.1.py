a=[45, 100, 4, 5, 99]
x=a[0]
for i in a:
    if i > x and i % 2 == 0:
        x=i
print(x)
