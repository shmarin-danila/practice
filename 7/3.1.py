from math import sqrt
a1=int(input())
b1=int(input())
a2=int(input())
b2=int(input())
def gip(a, b):
    c=sqrt(a**2+b**2)
    return c
a=gip(a1, b1)
b=gip(a2, b2)
if a<b:
    print("2 bolshe")
else:
    print("1 bolshe")
