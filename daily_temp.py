T = [73, 74, 75, 71, 69, 72, 76, 73]
out = []
for i in range(len(T)-1):
    print(T[i+1:])
    out.append(T.index(max(T[i+i:]))-T.index(T[i]))
print(T)
# k= int(input())
# print(k)