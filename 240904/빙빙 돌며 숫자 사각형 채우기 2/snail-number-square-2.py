n, m = map(int, input().split())

# 1->0 (d+3)%4

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

grid = [[0]*m for _ in range(n)]
x, y = 0, 0
grid[x][y] = 1
d = 1
for i in range(2, n*m+1):
    nx, ny = x + dx[d], y + dy[d]
    if not (0<=nx<n and 0<=ny<m and grid[nx][ny]==0):
        d = (d+3) % 4
        nx, ny = x + dx[d], y + dy[d]
    grid[nx][ny] = i
    x, y = nx, ny
    
for row in grid:
    print(*row)