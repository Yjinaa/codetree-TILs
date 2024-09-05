n = int(input())

ns = list(map(int, input().split()))

arr = []
ans = []

for i, num in enumerate(ns):
    arr.append(num)
    if i == 0:
        ans.append(num)

    if i % 2 != 0:
        idx = len(arr)//2
        ans.append(arr[idx])

print(*ans)