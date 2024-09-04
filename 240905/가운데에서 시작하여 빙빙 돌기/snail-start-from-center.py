n = int(input())

x, y = n-1, n-1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

grid = [[0]*n for _ in range(n)]

grid[x][y] = n*n
d = 2
for i in range(n*n-1, 0, -1):
    nx, ny = x + dx[d], y + dy[d]
    if not (0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0):
        d = (d+1) % 4
        nx, ny = x + dx[d], y + dy[d]
    grid[nx][ny] = i
    x, y = nx, ny

for row in grid:
    print(*row)