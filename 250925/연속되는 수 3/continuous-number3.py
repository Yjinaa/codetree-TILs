N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

cur = 1
longest = 1
for i in range(N):
    if i > 0 and arr[i] * arr[i-1] > 0:
        cur+= 1
    else:
        cur = 1
    longest = max(longest, cur)

print(longest)