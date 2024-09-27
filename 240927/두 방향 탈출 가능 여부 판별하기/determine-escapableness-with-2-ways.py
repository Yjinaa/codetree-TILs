n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dxs = [1,0]
dys = [0,1]

def dfs(x,y):
    visited[x][y] = True
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y+dy

        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != 0 and visited[nx][ny] != True:
            if nx == n-1 and ny == m-1:
                return 1
            visited[nx][ny] = True
            dfs(nx, ny)
    return 0

print(dfs(0,0))