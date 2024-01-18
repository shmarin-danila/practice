def fun():
    s=[int(i) for i in input() if int(i)]
    return s[::2]
print(fun())
