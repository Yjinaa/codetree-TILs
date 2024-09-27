n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dxs = [1,0]
dys = [0,1]

def dfs(x,y):
    visited[x][y] = 1
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y+dy

        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != 0 and visited[nx][ny] != True:
            visited[nx][ny] = 1

visited[0][0] = 1
dfs(0,0)
pirnt(visited[n-1][m-1])