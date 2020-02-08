x = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
x_m = {}
for i in x:
    if i not in x_m:
        x_m[i] = 0
    x_m[i] += 1
s = ''
print(x_m)
for i,j in x_m.items():
    s+= i
    if j != 1:
        s+=str(j)
    
print(len(s))
