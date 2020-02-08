factor = []
num = 1
for i in range(1,int(1+(num**0.5))):
    if num%i==0:
        factor.append(i)
        factor.append(num//i)
print(factor)
