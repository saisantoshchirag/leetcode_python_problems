inr = [0,1,0,1,0,1,99]
res = inr[0]
for i in range(len(inr)):
    res = res ^ inr[i]

s = "abcd"
t = "abcde"
return list(set(t).difference(set(s)))[0]
