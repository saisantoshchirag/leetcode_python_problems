n = 6
factor = [i for i in range(1,1+n//2) if n%i==0]
print(sum(factor)==n)
