s = [1,1,0,1,0,1,1,0,1,1,1,1,1]
t = ''.join(list(map(str,s)))
print(t)
t = t.split('0')
print(t)
print(max(t))
