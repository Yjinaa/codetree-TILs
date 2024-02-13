li = [0 for _ in range(9)]
n = int(input())
ns = list(map(int, input().split()))

for elem in ns:
    li[int(elem)-1] += 1

for elem in li:
    print(elem)