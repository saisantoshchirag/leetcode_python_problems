from itertools import combinations
ar = [2,3,5]
tar = 15
out = []
for i in ar:
    if tar%i==0:
        out.append([i]*(tar//i))
print(out)
arr = []
for r in range(0,len(ar)+1):        
    arr += list(combinations(ar, r))
print(arr)
