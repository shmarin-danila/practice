a = int(input("A: "))
b = int(input("B: "))
if a>b:
    for i in range(a, b + 1, -1):
        if i % 2 != 0:
          print(i)
else print("A<B")
