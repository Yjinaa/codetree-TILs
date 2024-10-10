import sys

n = int(input())
ns = list(map(int, input().split()))

max_val = ns[0]
cur_sum = ns[0]

for i in range(1,n):
    if cur_sum < 0:
        cur_sum = 0
    cur_sum += ns[i]
    if cur_sum > max_val:
        max_val = cur_sum


print(max_val)