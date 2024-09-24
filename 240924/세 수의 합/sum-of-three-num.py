# 하나의 수를 정하고, 그거 뺀 나머지 수에서 two sum

from collections import defaultdict

n,k = map(int, input().split())

nums = sorted(list(map(int, input().split())))

# -1, 1, 1, 2, 4

cnt = 0

for i in range(n):
    left = i+1
    right = len(nums)-1
    while left < right:
        target = nums[i] + nums[left] + nums[right]
        if target == k:
            cnt += 1
            left += 1
        elif target > k:
            right -= 1
        elif target < k:
            left += 1
    
print(cnt)