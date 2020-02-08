s = "CONTEST IS COMING"
st = s.split(' ')
max_len = len(max(st,key=len))
arr = []
for i in range(len(st)):
    if len(st[i])<max_len:
        st[i] += ' ' * (max_len-len(st[i]))
print(st)
m = [[i for i in word] for word in st]
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print(rez)
out = []
for i in rez:
    out.append(''.join(i).rstrip())
print(out)