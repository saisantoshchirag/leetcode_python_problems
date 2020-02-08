import profile
n= 5
a=2
b=11
c=13
l_a = set([a*i for i in range(1,n+1)])
l_b = set([b*i for i in range(1,n+1)])
l_c = set([c*i for i in range(1,n+1)])
print(l_a)
print(l_b)
print(l_c)
out = sorted(list((l_a.union(l_b)).union(l_c)))
print(out[n-1])
print(out)
