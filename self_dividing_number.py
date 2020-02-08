left,right = 1,22
out = []
for i in range(left,right+1):
    flag = 1
    if '0' in str(i):
        continue
    else:
        for j in str(i):
            if i%int(j)!=0:
                flag = 0
        if flag:
            out.append(i)
print(out)
