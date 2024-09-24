from collections import defaultdict
n, k = map(int, input().split())

cnt = 0
nums = list(map(int, input().split()))
complements = defaultdict(int)
for num in nums:
    complement = k-num
    if complement in complements:
        cnt += 1
    else:
        complements[num] = complement

print(cnt)