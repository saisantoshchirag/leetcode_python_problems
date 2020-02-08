import numpy as np
import pandas
# from itertools import permutations
num_people = 4
candies = 7
arr = [0] * num_people
cur, ind = 1, 0
while candies>0:
    candies -= cur
    arr[ind] += cur
    if ind+1==num_people:
        ind = -1
    ind+=1
    cur = min(candies, cur + 1)
    # print('i',i)
    # print('p',p)
print(arr)
