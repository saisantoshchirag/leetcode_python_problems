s = '1+-1i'
t = '1+-1i'
s = s.split('+')
t = t.split('+')

real = (int(s[0]) * int(t[0])) - (int(t[1][:-1]) * int(s[1][:-1]))
img = (int(s[1][:-1]) * int(t[0])) + (int(t[1][:-1]) * int(s[0]))
out = str(real) + '+' + str(img) + 'i'
print(out)