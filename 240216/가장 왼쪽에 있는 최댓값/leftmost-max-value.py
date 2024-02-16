import sys
n = int(input())
ns = list(map(int, input().split()))
maxes = []
maxv = -sys.maxsize
while maxv != ns[0]:
    maxv = -sys.maxsize
    for elem in ns:
        if elem > maxv:
            maxv = elem
    maxes.append(ns.index(maxv)+1)
    if len(ns[:ns.index(maxv)]) <= 1:
        print(*maxes)
    else:
        ns = ns[:ns.index(maxv)]