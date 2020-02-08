group = [3,3,3,3,3,1,3]
maps = {}
for i in range(len(group)):
    if group[i] not in maps:
        maps[group[i]] = [0,[]]
        
    maps[group[i]][0] += 1
    maps[group[i]][1].append(i)
print(maps)
out = []
for i in maps:
    print(maps[i])
    t = maps[i][0] // i
    if t==1:
        out.append(maps[i][1])
    else:
        for j in range(t):
            out.append(maps[i][1][i*j:i*(j+1)])
print(out)
