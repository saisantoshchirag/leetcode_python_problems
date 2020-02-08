S = "A x gij T Ka Stsl UTK kqdc A"
out = S.split()
o  = ''  
print(out)
for i in range(len(out)):
    if out[i][0] in 'aeiouAEIOU':
        o = o + out[i] + 'ma' + 'a'*(i+1)
    else:
        o += out[i][1:] + out[i][0] + 'ma' + 'a'*(i+1)
    if i!=len(out)-1:
        o += ' '
print(o)
