import collections
strs = ["eat","tea","ate","nat","tan","bat"]
out = {}
for i in strs:
    x = str(sorted(i))
    if x not in out:
        out[x] = []
    out[x].append(i)
print(out.values())
# ans = collections.defaultdict(list)
# print(ans)
# for s in strs:
#     ans[tuple(sorted(s))].append(s)
# print(ans.values())