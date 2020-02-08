#Given an integer n, return any array containing n unique integers such that they add up to 0.
n = 4
out = []
for i in range(1,n//2+1):
    out.append(i)
    out.append(-i)
print(out)
