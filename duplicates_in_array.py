out  = {}
nums = [4,3,2,7,8,2,3,1]
for i in nums:
    if i not in out:
        out[i] = 0
    out[i] += 1
o = []
for i,j in out.items():
    if j==2:
        o.append(i)
print(o)
