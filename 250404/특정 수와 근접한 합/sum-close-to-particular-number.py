import sys
N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
ans = sys.maxsize
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        cur_sum = 0
        for k in range(N):
            if k != i and k != j:
                cur_sum += arr[k]
        ans = min(ans, abs(cur_sum-S))

print(ans)
        