out = [0,1,1]
for i in range(23):
    out.append(sum(out[-3:]))
#print(out[-1])
out1 = [0,1]
for i in range(1):
    out1.append(sum(out1[-2:]))
print(out1)
