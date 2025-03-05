n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

# 가능한 모든 구간들에 대해
# 구간의 시작점이 0 ~ n-k 까지 일 때

ans = 0

for i in range(n-k+1):
    value = sum(arr[i:i+k])

    ans = max(value,ans)

print(ans)