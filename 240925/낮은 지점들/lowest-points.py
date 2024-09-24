from collections import defaultdict

n = int(input())

d = defaultdict(list)

for i in range(n):
    x, y = map(int, input().split())
    if x not in d:
        d[x] = y
    else:
        d[x] = min(y, d[x])

sum_val = 0
for val in d.values():
    sum_val += val

print(sum_val)