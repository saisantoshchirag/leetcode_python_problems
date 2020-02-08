s = 'abccccdd'
out = {}
for i in s:
    if i not in out:
        out[i] = 0
    out[i]+=1
print(out)
c = 0
for i in out.values():
    if i%2==0:
        c += i
    elif i>1 and i%2==1:
        c += (i//2)*2
if 1 in out.values():
    c += 1
print(c)

n = 11
for i in range(n):
    a,b = i,n-i
    print(a,b)
    if ('0' not in str(a)) and ('0' not in str(b)):
        print(a,b)