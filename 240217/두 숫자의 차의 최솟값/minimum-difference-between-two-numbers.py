n = int(input())
import sys

ns = list(map(int, input().split()))

ans = []

for i in range(n):
    for j in range(i+1, n):
        answer = ns[i] - ns[j]
        if answer < 0:
            answer = -answer
        ans.append(answer)
minv = sys.maxsize
for elem in ans:
    if elem < minv:
        minv = elem

print(minv)