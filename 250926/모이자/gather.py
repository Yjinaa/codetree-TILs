import sys
import math

n = int(input())
arr = list(map(int, input().split()))

min_dist = sys.maxsize
for i in range(n):
    dist = 0
    for j in range(n):
        if i == j:
            continue
        dist += arr[j] * abs(j-i)
    min_dist = min(dist, min_dist)

print(min_dist)


# Please write your code here.