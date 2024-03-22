import sys
n = int(input())
ns = list(map(int, input().split()))
minimum = sys.maxsize

for i in range(n):
    sum_dist = 0
    for j in range(n):
        sum_dist += abs(j-i) * ns[j]

    minimum = min(minimum, sum_dist)


print(minimum)