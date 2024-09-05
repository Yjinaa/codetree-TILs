n = int(input())

ns = list(map(int, input().split()))

for i in range(n):
    if i % 2 == 0:
        arr = ns[:i+1]
        mid = len(arr)//2
        print(sorted(arr)[mid], end=" ")