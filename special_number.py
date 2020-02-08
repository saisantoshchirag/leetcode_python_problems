from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

print(list(powerset([1,2,3])))
def get_subset(s):
  power_set=[[]]
  for elem in s:
    for sub_set in power_set:
      power_set=power_set+[list(sub_set)+[elem]]
  return power_set


t = int(input())
for _ in range(t):
    n = int(input())
    f = "SPECIAL"
    factors = [i for i in range(1,1+n//2) if n%i==0]
    if sum(factors)<n:
        f = "NOT SPECIAL"
    subsets = list(powerset(factors))
    if sum(factors) >n:
        for i in subsets:
            if sum(i) == n:
                f = "NOT SPECIAL"
    print(f)
