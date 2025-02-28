n = int(input())
grid = [[0] * n for _ in range(n)]

# Please write your code here.

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = n-1, n-1
d = 2

for i in range(n*n, 0, -1):
    grid[x][y] = i
    nx, ny = x + dx[d], y + dy[d]

    if not (0 <= nx < n and 0 <= ny < n) or grid[nx][ny] != 0:
        d = (d+1)%4
    x, y = x + dx[d], y + dy[d]

for row in grid:
    print(*row)
