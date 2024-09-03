n, m = map(int, input().split())

grid = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = 0
grid[0][0] = 1
x, y = 0, 0

for i in range(2, n*m + 1):
    visited[x][y] = True
    nx, ny = x + dx[d], y + dy[d]
    if (not (0 <= nx < n and 0 <= ny < m)) or (visited[nx][ny] == True):
        d = (d + 1) % 4
        nx, ny = x + dx[d], y + dy[d]
    grid[nx][ny] = i
    visited[nx][ny] = True
    x, y = nx, ny
    
for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()