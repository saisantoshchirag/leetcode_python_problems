n = int(input())
numbers = input()
l = list(map(int,numbers.split()))
rev = 0
count = 0
for i in range(len(l)):
    cur = l[i]
    for j in range(i+1,len(l)):
        rev += abs(cur-l[j])
print(rev)
