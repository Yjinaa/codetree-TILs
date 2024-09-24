# 하나의 수를 정하고, 그거 뺀 나머지 수에서 반복

from collections import Counter

n,k = map(int, input().split())

nums = list(map(int, input().split()))
complements = Counter(nums)

cnt = 0

for i in range(n):
    complements[nums[i]] -= 1

    for j in range(i):
        diff = k - nums[i] - nums[j]
        if diff in complements:
            cnt += complements[diff]
print(cnt)