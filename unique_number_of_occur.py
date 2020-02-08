out = {}
arr =  [-3,0,1,-3,1,1,1,-3,10,0]
for i in arr:
    
    if i not in out:
        out[i] = 0
    out[i] += 1
y = list(out.values())
print(y)
print(list(set(y)))
print(len(y)==len(list(set(y))))
