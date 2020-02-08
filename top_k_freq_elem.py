nums = [1,1,1,2,2,3]
k = 2
out = {}
for i in nums:
    if i not in out:
        out[i] = 0
    out[i] += 1
print(out)
out1 = {k: v for k, v in sorted(out.items(),key = lambda x:x[1],reverse=True)}
res =  list(out1.keys())
print(res)
