n = int(input())

# Please write your code here.
ans = [0] * 203
for _ in range(n):
    a, b = map(int, input().split())
    a, b = a+100, b+100
    for i in range(a, b+1):
        ans[i] += 1

print(max(ans))