import pandas as pd

f1 = pd.read_csv('e-z curl bar1.csv',header=0,encoding = 'unicode_escape')
f2 = pd.read_csv('e-z curl bar2.csv',header=0,encoding = 'unicode_escape')
f3 = pd.read_csv('e-z curl bar3.csv',header=0,encoding = 'unicode_escape')
#print(f1)
l1 = f1['Field1']
print(l1)
img = []
for i in l1:
    temp = i.split("src=")
    temp1 = temp[1].split(" class")
    #print(temp1.spl)
    img.append(temp1[0].split('"')[1])
f4 = pd.DataFrame(img)
print(type(f4))
print(len(f1))
print(len(f3))
print(len(f2))
data = [f4,f2,f3]
result = pd.concat(data,ignore_index=True,axis=1)
print(type(result))
result.to_csv('e-z curl bar.csv',index_label=False,index=False)