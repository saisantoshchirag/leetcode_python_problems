import math
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def heron( p1, p2, p3):
    a = distance(p1, p2)
    b = distance(p1, p3)
    c = distance(p2, p3)
    s = (a + b + c) / 2
    res = s * (s - a) * (s - b) * (s - c)
    return 0 if res < 0 else math.sqrt(res)

points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
ar = []
for i in range(len(points)-2):
    for j in range(i+1,len(points)-1):
        for k in range(j+1,len(points)):
            ar.append(heron(points[i],points[j],points[k]))
            print(points[i],points[j],points[k])
print(ar)