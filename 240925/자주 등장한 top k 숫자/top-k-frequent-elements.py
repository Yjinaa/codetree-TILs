n, k = map(int, input().split())

nums = list(map(int, input().split()))

from collections import Counter

c = Counter(nums)
mc = sorted(c.most_common(k), key=lambda x:(-x[1],-x[0]))
for elem in mc:
    print(elem[0], end=" ")