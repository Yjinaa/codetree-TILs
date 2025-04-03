import sys 

n = int(input())
A = list(map(int, input().split()))

# Please write your code here.

min_dist = sys.maxsize

for i in range(n):
    cur_dist = 0
    for j in range(n):
        if i == j:
            continue
        cur_dist += abs(i-j)*A[j]
    min_dist = min(cur_dist, min_dist)

print(min_dist)