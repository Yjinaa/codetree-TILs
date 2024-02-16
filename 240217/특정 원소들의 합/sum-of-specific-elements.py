arr = [list(map(int, input().split())) for _ in range(4)]
ans = 0

for j in range(4):
    for i in range(j,4):
        ans += arr[i][j]

print(ans)