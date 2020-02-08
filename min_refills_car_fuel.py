def minRefills(x,n,l):
    numRefills = 0
    cur = 0
    while cur<=n:
        lastRefill = cur
        print(cur)
        while (cur<=n and x[cur+1]-x[lastRefill]<=l):
            cur += 1
        if cur==lastRefill:
            return 'impossible'
        if cur<=n:
            numRefills += 1
        print(numRefills)

    return numRefills

print(minRefills([0,200,375,550,750,950],950,400))