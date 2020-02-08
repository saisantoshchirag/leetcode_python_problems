a = 8
b = 3
c = 5
a = bin(a)[2:]
b = bin(b)[2:]
c = bin(c)[2:]
if len(a)<len(b):
    a = '0'*(len(b)-len(a)) + a
else:
    b = '0'*(len(a)-len(b)) + b
if len(c)<len(a):
    c = '0' * (len(a) - len(c))
else:
    a = '0' * ( len(c) - len(a)) + a
    b = '0' * ( len(c) - len(b)) + b
coun = 0
print(a)
print(b)
print(c)
for i in range(len(a)):
    if int(a[i]) | int(b[i]) == int(c[i]):
        continue
    elif (a[i]!=b[i]) and c[i]=='0':
        coun += 1
    elif (a[i]==b[i]=='0') and c[i] == '1':
        coun += 1
    elif (a[i] == b[i] == '1') and c[i] == '0':
        coun += 2
print(coun)