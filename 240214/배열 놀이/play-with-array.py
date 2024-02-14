n, q = map(int, input().split())

ns = list(map(int, input().split()))

for i in range(q):
    qs = list(map(int, input().split()))
    if qs[0] == 1:
        print(ns[qs[1]-1])
    elif qs[0] == 2:
        try:
            print(ns.index(qs[1]) + 1)
        except:
            print(0)
    else:
        for i in range(qs[1], qs[2]+1):
            print(ns[i-1], end=" ")