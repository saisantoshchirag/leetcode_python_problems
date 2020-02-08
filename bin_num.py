n = 10
n_b = bin(n)[2:]
c = 0
for i in range(len(n_b)-1):
    if n_b[i] != n_b[i+1]:
        c+=1
print(c)
