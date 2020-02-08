S = input()
t = input()
ans = []
for i in S:
    if i != '#':
        ans.append(i)
    if i=='#' and len(ans)!=0:
        print('inif',ans)
        ans.pop()
        print('inif',ans)
    elif i=='#' and len(ans)==0:
        continue
    print(ans)
sans = ''.join(ans)
tans = []
for i in t:
    if i!='#':
        tans.append(i)
    if i=='#' and len(tans)!=0:
        tans.pop()
    elif i=='#' and len(tans)==0:
        continue
tans1 = ''.join(tans)
print(sans)
print(tans1)
print(sans == tans1)