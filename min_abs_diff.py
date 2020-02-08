arr = [4,2,1,3]
out = {}
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if abs(arr[j]-arr[i]) not in out:
            out[abs(arr[j]-arr[i])] = []
        out[abs(arr[j]-arr[i])].append([min(arr[i],arr[j]),max(arr[i],arr[j])])
print(out)
out1 = sorted(out)
print(sorted(out[out1[0]]))
