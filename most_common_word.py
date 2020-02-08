paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.".lower()
paragraph = paragraph.replace(',','')
paragraph = paragraph.replace('.','')
print(paragraph)
para = paragraph.rstrip('.').split()
banned = ['hit']
print(para)
maxi = para[0]
for i in para:
    print(maxi)
    print(para.count(i),para.count(maxi))
    if para.count(i) > para.count(maxi) and i not in banned:
        print(i)
        maxi = i
print(maxi)
