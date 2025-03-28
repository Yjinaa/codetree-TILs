n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

cur = 0
longest = 0

for i in range(n):
    if i >= 1 and arr[i] > arr[i-1]:
        cur += 1
    else:
        cur = 1
    longest = max(longest, cur)

print(longest)
        