from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def bfs(x,y):
    max_val = 0
    max_x = -1
    max_y = -1
    standard = grid[x][y]
    queue = deque([(x,y)])
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    while queue:
        x,y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != True and grid[nx][ny] < standard:
                if (max_val, -max_x, -max_y) < (grid[nx][ny], -nx, -ny):
                    max_val, max_x, max_y = grid[nx][ny], nx, ny
                visited[nx][ny] = True
    if max_x != -1:
        return max_x, max_y
    else:
        return x,y

x,y = map(int, input().split())
x,y = x-1, y-1

for _ in range(k):
    x,y = bfs(x,y)

print(x+1,y+1)