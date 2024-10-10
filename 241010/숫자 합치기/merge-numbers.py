import heapq
n = int(input())
ns = sorted(list(map(int, input().split())))
heapq.heapify(ns)

tv = 0
cur_sum = []

while len(ns) >= 2:
    min1, min2 = heapq.heappop(ns), heapq.heappop(ns)
    v = min1 + min2
    heapq.heappush(ns, v)
    tv += v

print(tv)