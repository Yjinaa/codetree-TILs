n, k = map(int, input().split())

bs = [0] * (n+1)

for i in range(k):
    a, b = map(int, input().split())
    for j in range(a,b+1):
        bs[j] += 1

print(max(bs))
