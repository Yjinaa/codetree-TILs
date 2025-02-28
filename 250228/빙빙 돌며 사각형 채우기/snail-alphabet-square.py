n, m = map(int, input().split())

# Please write your code here.

grid = [[0 for _ in range(m)] for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
d = 0

for i in range(65, 65+m*n):
    grid[x][y] = chr(i)

    nx, ny = x + dx[d], y + dy[d]
    if not (0 <= nx < n and 0 <= ny < m) or grid[nx][ny] != 0:
        d = (d+1)%4
    x, y = x + dx[d], y + dy[d]


for row in grid:
    print(*row)