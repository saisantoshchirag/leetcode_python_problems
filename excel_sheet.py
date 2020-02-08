d = {}
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    d[i] = ord(i)-64
print(d)
f = 'A'
num = 0
for i in range(len(f)):
    num += 26**(len(f)-1-i) * d[f[i]]
print(num)
