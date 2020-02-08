arr = [1,2,3,1,2,3]
out = {}
k=2
for i in range(len(arr)):
    if arr[i] not in out:
        out[arr[i]] = [0,[]]
    out[arr[i]][0] += 1
    out[arr[i]][1].append(i)
for j in out.values():
    if j[0] == 1:
        continue
    elif j[0]>1:
        for a in range(len(j[1])-1):
            if abs(j[1][a]-j[1][a+1]) <= k:
                print(True)
s = 'cbbd'
x = 0
r = ''
if r:
    print(False)
else:
    print(True)
for i in range(len(s)):
    for j in range(i+1,len(s)):
        print(s[i:j+1])
        if s[i:j+1] == s[i:j+1][::-1] and len(s[i:j+1]) > len(r):
            r = s[i:j+1]
        x+=1
print(x)
print(r)
