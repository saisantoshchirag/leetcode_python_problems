a1 =  ["tarp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
res = []
for i in a1:
    for j in a2:
        if i in j:
            print('yes')
            res.append(i)
print(sorted(list(set(res))))
