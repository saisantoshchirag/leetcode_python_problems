import math
nums = [19]
thresh = 5
num = 1
fact = [math.ceil(i/num) for i in nums]
print(sum(fact))
while sum(fact)>thresh:
    num += 1
    fact = [math.ceil(i/num) for i in nums]

def smallestDivisor( nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        num = 1
        fact = [math.ceil(i/num) for i in nums]
        while sum(fact)>threshold:
            num += 1
            fact = [math.ceil(i/num) for i in nums]
        return num
print(smallestDivisor([19],5))
