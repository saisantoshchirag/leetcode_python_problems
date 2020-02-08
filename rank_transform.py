arr = [100,100,100]
arr1 = sorted(arr)
out = {}
k = 1
for i in arr1:
    if i not in out:
        out[i] = k
        k += 1
t = []
for i in arr:
    t.append(out[i])
print(t)