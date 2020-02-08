p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]

def distance(p1,p2):
    return (abs(p1[0]-p2[0])**2+abs(p1[1]-p2[1])**2)**0.5
arr = []
arr.append(distance(p1,p2))
arr.append(distance(p3,p2))
arr.append(distance(p4,p2))
arr.append(distance(p3,p4))
arr.append(distance(p1,p4))
arr.append(distance(p1,p3))
print(len(set(arr)))