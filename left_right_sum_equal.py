arr = [0,0,2,0]
left = 0
right = sum(arr)
#print(left,right)
for i in range(0,len(arr)):
    left += arr[i]
#    right = right + arr[i] - left
    if left==right+arr[i]-left:
        print('i',i)
        break

