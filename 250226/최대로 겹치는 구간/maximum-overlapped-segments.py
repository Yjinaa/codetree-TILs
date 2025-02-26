n = int(input())
# segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = [0] * 201

for i in range(n):
    start, end = tuple(map(int, input().split()))
    for i in range(start, end):
        ans[i] += 1


print(max(ans))