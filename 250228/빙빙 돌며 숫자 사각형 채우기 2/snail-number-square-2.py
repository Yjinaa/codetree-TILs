n, m = map(int, input().split())

grid = [[0 for _ in range(m)] for _ in range(n)]
# Please write your code here.

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
d = 1

for i in range(1,n*m+1):
    grid[x][y] = i
    nx, ny = x + dx[d], y + dy[d]
    if not (0 <= nx < n and 0 <= ny < m) or (grid[nx][ny]!=0):
        d = (d+3)%4
    x, y = x + dx[d], y + dy[d]
for row in grid:
    print(*row)


        