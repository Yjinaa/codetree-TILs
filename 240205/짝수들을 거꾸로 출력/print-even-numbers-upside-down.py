n = int(input())

nums = list(map(int, input().split()))

arr = []

for elem in nums:
    if elem % 2 == 0:
        arr.append(elem)
    else:
        continue

print(*arr[::-1])