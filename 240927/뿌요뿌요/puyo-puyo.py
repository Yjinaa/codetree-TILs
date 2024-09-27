# 10:47
n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def dfs(x,y):
    blocks = 1
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != True and grid[nx][ny] == grid[x][y]:
            visited[nx][ny] = True
            blocks += dfs(nx,ny)
    return blocks

block_region = 0
total_block_nums = []
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            blocks = dfs(i,j)
            if blocks >= 4:
                block_region += 1
                total_block_nums.append(blocks)
            else:
                continue

print(block_region, max(total_block_nums))