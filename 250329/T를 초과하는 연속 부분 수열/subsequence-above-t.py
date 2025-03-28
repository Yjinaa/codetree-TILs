n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

cur, longest = 0, 0

for i in range(n):
    if arr[i] > t:
        cur += 1
    else:
        cur = 0
    longest = max(longest,cur)

print(longest)