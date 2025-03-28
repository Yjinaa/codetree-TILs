N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

cur = 1
longest = 0
for i in range(N):
    if i == 0 or arr[i] * arr[i-1] < 0:
        longest = max(cur, longest)
        cur = 0
    cur += 1

longest = max(longest, cur)

print(longest)