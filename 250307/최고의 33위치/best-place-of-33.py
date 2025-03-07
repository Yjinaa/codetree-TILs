n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0

for i in range(n):
    cnt = 0
    for row in range(i,i+3):
        for col in range(i,i+3):
            if 0 <= row < n and 0 <= col < n and grid[row][col] == 1:
                cnt += 1
    ans = max(cnt,ans)

print(ans)