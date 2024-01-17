s = "He rarely rides public transport"
s=s.lower()
b=s.split()
for i in range(len(b)):
    a=b[i]
    b[i]=sorted(a)
s=' '.join(''.join(l) for l in b)
print(s)    
