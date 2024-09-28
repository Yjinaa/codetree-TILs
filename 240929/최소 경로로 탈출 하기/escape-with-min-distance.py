from collections import deque
n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
escaped = False
def bfs():
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] != True and grid[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                grid[nx][ny] = grid[x][y] + 1


grid[0][0] = 0
queue = deque([(0,0)])
bfs()
if visited[n-1][m-1] == True:
    print(grid[n-1][m-1])
else:
    print(-1)