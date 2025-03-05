import sys

n = int(input())
A = list(map(int, input().split()))

ans = sys.maxsize
for i in range(n):
    dist = 0
    for j in range(n):
        dist += abs(i-j) * A[j]
    
    ans = min(dist, ans)

print(ans)