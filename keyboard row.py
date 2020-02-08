def isRow(word):
    r1 = 'qwertyuiop'
    r2 = 'asdfghjkl'
    r3 = 'zxcvbnm'
    x = set()
    for i in word:
        if i.lower() in r1:
            x.add(1)
        elif i.lower() in r2:
            print('r2')
            x.add(2)
        elif i.lower() in r3:
            x.add(3)
    print(x)
    return len(x)==1

print(isRow('dad'))
    
