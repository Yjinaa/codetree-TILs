N = int(input())

ns = list(map(int, input().split()))

nums = []
for i, n in enumerate(ns, start=1):
    nums.append((i,n))

nums.sort(key=lambda x:x[1])
locs = [0] * (N+1)
pos = [num[0] for num in nums]
for i, po in enumerate(pos, start=1):
    locs[po] = i

print(*locs[1:])