n,m = map(int, input().split())

nums = list(map(int, input().split()))

from collections import Counter

c = Counter(nums)

targets = list(map(int, input().split()))

for target in targets:
    print(c[target], end=" ")