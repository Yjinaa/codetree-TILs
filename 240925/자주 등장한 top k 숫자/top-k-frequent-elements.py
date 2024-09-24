n, k = map(int, input().split())

nums = list(map(int, input().split()))

from collections import Counter

c = Counter(nums)
mc = sorted(c.items(), key=lambda x:(-x[1],-x[0]))
for i in range(k):
    print(mc[i][0], end=" ")