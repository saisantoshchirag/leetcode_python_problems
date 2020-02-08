# cook your dish here
t = int(input())
for i in range(t):
    str1,str2 = list(input().split())
    if set(list(str1)) == set(list(str2)):
        print(-1)
    else:
        for i in str1:
            if i in str2:
                str1 = str1.replace(i,"")
                str2 = str2.replace(i,"")
        print(str1+str2)
