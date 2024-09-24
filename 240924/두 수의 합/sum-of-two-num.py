from collections import defaultdict
from collections import Counter
n, k = map(int, input().split())

cnt = 0
nums = list(map(int, input().split()))
complements = defaultdict(list)
for i,num in enumerate(nums):
    complement = k-num
    if complement in complements:
        cnt += len(complements[complement])
    complements[num].append(i)

print(cnt)