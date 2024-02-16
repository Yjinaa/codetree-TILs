import sys
n = int(input())
ns = list(map(int, input().split()))

while True:
    maxv = ns[0]
    for elem in ns:
        if elem > maxv:
            maxv = elem
    print(ns.index(maxv)+1, end=" ")
    if ns.index(maxv) == 0:
        break
    ns = ns[:ns.index(maxv)]