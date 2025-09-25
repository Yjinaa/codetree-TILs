n = int(input())
arr = [int(input()) for _ in range(n)]

cur, longest = 1,1
for i in range(n):
    if i > 0 and arr[i] == arr[i-1]:
        cur += 1
    else:
        cur = 1
    longest = max(longest, cur)

print(longest)