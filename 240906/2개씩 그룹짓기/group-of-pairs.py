n = int(input())

ns = list(map(int, input().split()))

ns.sort()

max_num = 0
for i in range(n):
    cur = ns[i] + ns[len(ns)-1-i]
    if cur > max_num:
        max_num = cur

print(max_num)