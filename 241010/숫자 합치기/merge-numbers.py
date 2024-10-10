n = int(input())
ns = sorted(list(map(int, input().split())))

tv = 0
cur_sum = []

while len(ns) >= 2:
    min1, min2 = ns.pop(ns.index(min(ns))), ns.pop(ns.index(min(ns)))
    v = min1 + min2
    ns.insert(0,v)
    tv += v

print(tv)