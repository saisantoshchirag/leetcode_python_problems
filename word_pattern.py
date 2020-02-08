pattern = "paper"
stri = "title"
def result(pattern):
    out1 = {}
    for i in range(len(pattern)):
        if pattern[i] not in out1:
            out1[pattern[i]] = [0,[]]
        out1[pattern[i]][0]+=1
        out1[pattern[i]][1].append(i)
    return out1
l1 = list(result(pattern).values())
l2 = list(result(stri).values())
print(l1==l2)

