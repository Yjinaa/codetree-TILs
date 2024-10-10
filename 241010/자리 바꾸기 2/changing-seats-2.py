from collections import defaultdict

n, k = map(int, input().split())

ks = [list(map(int, input().split())) for _ in range(k)]
ns = [0] + [i+1 for i in range(n)]
d = defaultdict(set)

for i in range(n):
    d[i+1].add(i+1)

for i in range(3):
    for seat in ks:
        ns[seat[0]], ns[seat[1]] = ns[seat[1]], ns[seat[0]]
        d[ns[seat[0]]].add(seat[1])
        d[ns[seat[1]]].add(seat[0])

for key in d:
    print(len(d[key]))