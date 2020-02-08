coordinates = [[1,5],[2,3],[3,4],[4,5],[5,6],[6,7]]
t1 = coordinates[0][1]
t2 = coordinates[0][0]
sl = []
x,y = 0,0
print(t1)
for i in range(len(coordinates)):
    if coordinates[i][1] == t1:
        y+=1
    if coordinates[i][0] == t2:
        x+=1
for i in range(len(coordinates)-1):
    if coordinates[i+1][0] - coordinates[i][0] != 0 and coordinates[i+1][1] - coordinates[i][1] != 0:
        sl.append((coordinates[i+1][1] - coordinates[i][1])/(coordinates[i+1][0] - coordinates[i][0]))      
print(sl)

