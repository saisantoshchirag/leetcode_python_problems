def get_subset(s):
  power_set=[[]]
  for elem in s:
    for sub_set in power_set:
      power_set=power_set+[list(sub_set)+[elem]]
  return power_set

subsets = get_subset([1,2,3,5,4])
print(len(get_subset([1,2,3,5,3])))
for i in subsets:
  print(i)