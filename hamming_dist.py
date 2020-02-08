x=3
y=1
b_x = bin(min(x,y))[2:]
b_y = bin(max(x,y))[2:]
c = 0
if len(b_x)!=len(b_y):
    b_x = '0' * (len(b_y)-len(b_x)) + b_x
    
for i in range(len(b_x)):
    c += int(b_x[i]) ^ int(b_y[i])
print(c)
