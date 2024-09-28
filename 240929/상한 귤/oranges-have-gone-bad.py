from collections import deque

n,k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def bfs():
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != True and grid[nx][ny] == 1:
                queue.append((nx,ny))
                visited[nx][ny] = True
                ans[nx][ny] = ans[x][y] + 1

queue = deque()
ans = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            queue.append((i,j))
            visited[i][j] = True

bfs()

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            print(-1, end=" ")
        else:
            if grid[i][j] == 2:
                print(0, end= " ")
            else:
                if visited[i][j] != True:
                    print(-2, end=" ")
                else:
                    print(ans[i][j], end=" ")
    print()