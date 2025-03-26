n, k = map(int, input().split())

# Please write your code here.

ans = [0 for _ in range(n+1)]

for i in range(k):
    a, b = map(int, input().split())
    for j in range(a,b+1):
        ans[j] += 1

print(max(ans))