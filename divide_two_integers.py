dend = -1
sor = -1
sign = 1
if sor<0:
    sign = -1*sign
    sor = abs(sor)
if dend < 0:
    sign = -1*sign
    dend = abs(dend)
quo = 0
while dend >= sor:
    dend -= sor
    quo += 1
print(quo*sign)