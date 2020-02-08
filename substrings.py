num = int(input())
string = input()
sub,final = [],''
if string == string[::-1]:
    final = string
else:
    for i in range(len(string)):
        for j in range(i,len(string)):
            if string[i:j+1] not in sub:
                sub.append(string[i:j+1])
    for i in sub:
        if i==i[::-1] and len(i)>=len(final):
            final = i
print(final)
