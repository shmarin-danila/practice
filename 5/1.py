s = "Ефрейтор Евлампий Ельников единственный ел ежевику"
s = s.lower()
b = s.split()
c = 0
for b in b:
    if b.startswith('е'):
        c += 1
print(c)
