n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

cur = 1
longest = 0
for i in range(n):
    if i == 0 or arr[i] != arr[i-1]:
        longest = max(longest, cur)
        cur = 0
    cur += 1

print(longest)