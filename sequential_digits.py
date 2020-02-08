n = 48
m = 37

mat = [[0 for _ in range(m)] for _ in range(n)]
ind = [[40,5]]

for [i,j] in ind:
    print(i,j)
    for a in range(m):
        mat[i][a] += 1
    for b in range(n):
        mat[b][j] += 1
print(mat)
c = 0
for x in sum(mat,[]):
    if x%2==1:
        c+=1
print(c)
