from collections import Counter
words = 'rkqodlw'
s2 = 'world'
s1c = Counter(words)
s2c = Counter(s2)
print(s1c)
print(s2c)
f = 1
for i,j in s2c.items():
    if i not in s1c:
        f = 0
    else:
        if j > s1c[i]:
            f = 0
print(f)
