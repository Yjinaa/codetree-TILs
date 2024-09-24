# 하나의 수를 정하고, 그거 뺀 나머지 수에서 two sum

from collections import defaultdict

n,k = map(int, input().split())

nums = sorted(list(map(int, input().split())))

# -1, 1, 1, 2, 4

cnt = 0

for i in range(n):
    for left in range(i + 1, n):  # i 다음 인덱스부터 시작
        for right in range(left + 1, n):  # left 다음 인덱스부터 시작
            target = nums[i] + nums[left] + nums[right]
            if target == k:
                cnt += 1

print(cnt)