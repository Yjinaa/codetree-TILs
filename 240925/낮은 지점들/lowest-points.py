from collections import defaultdict

n = int(input())

d = defaultdict(list)

for i in range(n):
    x, y = map(int, input().split())
    d[x].append(y)

ans = 0
for point in d:
    if len(d[point]) != 1:
        d[point] = [min(d[point])]
    ans += d[point][0]

print(ans)