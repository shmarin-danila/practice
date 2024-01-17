a=[8,13,3,54,6,512,89,40,16,2]
x=0
n=0
c=0
for i in range(len(a)):
  if x<a[i]:
    x=a[i]
for i in range(len(a)):
  if x>a[i]:
    n += 1
  else:
    if x<a[i]:
        c +=1
print(n," ",c)
