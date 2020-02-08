import math
points = [[3,1],[12,3],[3,1],[-6,-1]]
def slope(p1,p2):
    if p2[0]-p1[0] == 0:
        return math.inf
    return (p2[1]-p1[1])/(p2[0]-p1[0])
def dupicates(points):
    temp = []
    for i in points:
        if i not in temp:
            temp.append(i)
    return len(points) - len(temp),temp

dup,points_temp  = dupicates(points)
print(points_temp)
print('dup',dup)
slopes = []
for i in range(len(points_temp)):
    for j in range(i+1,len(points_temp)):
        slopes.append(slope(points[i],points[j]))
x = max(slopes,key=slopes.count)
print(x)
print(slopes)
fact_x = 2*(slopes.count(x))
print(fact_x)
fact = [(i,fact_x//i) for i in range(1,int(fact_x**0.5)+1) if fact_x%i==0]
print(fact)
for i,j in fact:
    if abs(i-j)==1:
        print(max(i,j)+dup)
