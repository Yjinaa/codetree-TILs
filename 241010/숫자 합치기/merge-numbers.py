n = int(input())
ns = sorted(list(map(int, input().split())))

tv = 0
cur_sum = []

while len(ns) >= 2:
    v = ns.pop(0) + ns.pop(0)
    ns.insert(0,v)
    tv += v
    ns.sort()

print(tv)