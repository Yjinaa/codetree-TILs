n, m = map(int, input().split())

# Please write your code here.

grid = [[0 for _ in range(m)] for _ in range(n)]
grid[0][0] = 1
x, y, d = 0, 0, 2
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(1, n*m):
    nx, ny = x + dx[d], y + dy[d]
    if not (0 <= nx < n and 0 <= ny < m) or grid[nx][ny] != 0:
        d = (d+3)%4
    x, y = x + dx[d], y + dy[d]
    grid[x][y] = i+1

for row in grid:
    print(*row)
