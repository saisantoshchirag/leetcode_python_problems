s = 'abcdefg'
k=2
r = ''
for i in range(0,len(s),2*k):
    r += s[i:i+k][::-1]
    r += s[i+k:i+2*k]
    if i>k and i < 2*k:
        print(i)
print(s)
print(r)
