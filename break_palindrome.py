pal = 'aba'
arr = list(pal)
arr1 = list(pal)
for i in range(len(arr)):
    if arr[i] != 'a':
        arr[i] = 'a'
        x = ''.join(arr)
        if x==x[::-1]:
            arr[i] = 'b'
        break
    if arr == arr1:
        arr[-1] = 'b'
print(arr)
