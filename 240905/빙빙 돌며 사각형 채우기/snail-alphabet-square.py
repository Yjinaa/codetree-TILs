n,m = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = 0
x, y = 0,0
grid = [[0]*m for _ in range(n)]
grid[x][y] = chr(65)

for i in range(66, 66+n*m-1):
    new_i = 65 + (i-65) % (91-65)
    nx, ny = x + dx[d], y + dy[d]
    if not(0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0):
        d = (d+1)%4
        nx, ny = x + dx[d], y + dy[d]
    grid[nx][ny] = chr(new_i)
    x, y = nx, ny

for row in grid:
    print(*row)