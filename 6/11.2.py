a=[8,13,3,54,6,512,89,40,16,2]
lis=[]
for i in range(len(a)):
    if a[i] % 2 == 0 and a[i]<=10 :
     lis.append(a[i])
if len(lis) == 0:
     print('takix chisel nety')

lis.sort()
print(lis)
