n = 31
s  = bin(n)[2:]
print(s)
ans = 0
i = 0
j  = 0
while j<len(s):
    if s[i] == '1' and s[j] == '1':
        ans = max(ans,j-i)
        print(i,j)
        i = j
        j += 1
    else:
        j += 1
print(ans)