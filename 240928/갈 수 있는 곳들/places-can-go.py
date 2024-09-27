from collections import deque

n, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def bfs():
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != True and grid[nx][ny] != 1:
                queue.append((nx,ny))
                visited[nx][ny] = True

for _ in range(k):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    queue = deque([(x,y)])
    visited[x][y] = True
    bfs()

print(sum(sum(row) for row in visited))