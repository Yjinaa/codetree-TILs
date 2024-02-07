ns = list(map(int, input().split()))

for i in range(2,10):
    ns.append(ns[-1] + 2*ns[-2])

print(*ns)