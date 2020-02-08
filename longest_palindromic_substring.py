r = ''
s = 'babad'
if len(s)<=1:
    # return s
    print(s)
if s==s[::-1]:
    # return s
    print(s)
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i:j+1] == s[i:j+1][::-1] and len(s[i:j+1]) > len(r):
            r = s[i:j+1]
if not r:
    print(s[0])
    # return s[0]
else:
    print(r)
    # return r