s = '123456789'
arr = []
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        arr.append(int(s[i:j]))
print(arr)
arr = sorted(arr)
print(len(arr))
print(arr)