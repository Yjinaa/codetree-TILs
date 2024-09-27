# 10:14
n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
k = 1
max_regions = 0
max_k = 0

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def dfs(x,y):
    visited[x][y] = True
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] != True and grid2[nx][ny] != 1:
            visited[nx][ny] = True
            dfs(nx,ny)

while True:
    grid2 = [[0]*m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    flooded = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] <= k:
                grid2[i][j] = 1
                flooded += 1
    if flooded == n*m:
        if max_regions == 0:
            print(k)
            mak_k = k
            print(max_k)
        break

    regions = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid2[i][j] == 0:
                dfs(i,j)
                regions += 1
    if regions > max_regions:
        max_k = k 
        max_regions = regions
    k += 1

print(max_k, max_regions)