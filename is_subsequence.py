s = "axc"
t = "ahbgdc"
t_l = list(s)
print(t_l)
te = []
for i in s:
    try:
        te.append(t.index(i))
    except:
        pass
print(te==sorted(te))
print(te)
