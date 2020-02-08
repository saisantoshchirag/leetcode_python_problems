nums = [3,2,2,3]
t = 3
for i in nums:
    if i!=t:
        continue
    if i == t:
        ind = nums.index(i)
        nums[:] = nums[:i] + nums[i+1:]
        print(i,nums)
    print(i)
print(nums)

