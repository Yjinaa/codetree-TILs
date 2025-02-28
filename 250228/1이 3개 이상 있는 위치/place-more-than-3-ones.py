n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

cur_dir = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ans = 0

for row in range(n):
    for col in range(n):
        cnt = 0
        for i in range(4):
            nx, ny = row + dx[i], col + dy[i]
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            ans += 1

print(ans)

