n = 5
arr = []
for i in range(n):
    arr.insert(0,chr(ord('a')+i))
print(arr)
out = []
for i in range(len(arr)):
    out.append('-'.join(arr[:i+1]))
print(out)
arr = [12,9,61,5,14]
x = []
for i in arr:
    if i>0 and str(i)==str(i)[::-1]:
        x.append(True)
    else:
        x.append(False)
print(x)
y = [True if i>0 and str(i)==str(i)[::-1] else False for i in arr ]