from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    c= 0 
    x = list(map(int,stdin.readline().split()))
    #print(fun(x)*7)
    if 2*x[0]==x[1] and 2*x[1]==x[2]:
        print(x[0]*7)
    else:    
        for i in range(1,x[0]+1):
            if i<=x[0] and i*2<=x[1] and i*4<=x[2]:
                c+=1
        print(c)
