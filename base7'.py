num = 100
res = ''
while num>0:
    res += str(num%7)
    num = num//7
print(res)
