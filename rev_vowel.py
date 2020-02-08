s = "hello"
i = 0
j = len(s)-1
print(s[j])
def swap(s,i,j):
    print(s,i,j)
    s = list(s)
    s[i],s[j] = s[j],s[i]
    return ''.join(s)

while i<j:
    if s[i] not in 'aeiou':
        i+=1
        print('T')
        continue
        
    elif s[j] not in 'aeiou':
        j-=1
        print('Y')
        continue

    s = swap(s,i,j)
    i+=1
    j-=1
print(s)
    
