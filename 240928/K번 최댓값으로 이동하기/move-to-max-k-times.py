from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def bfs(x,y):
    standard = grid[x][y]
    available_paths = []
    queue = deque([(x,y)])
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    while queue:
        x,y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != True and grid[nx][ny] < standard:
                available_paths.append((nx,ny,grid[nx][ny]))
                queue.append((nx,ny))
                visited[nx][ny] = True
    return available_paths

x,y = map(int, input().split())
x,y = x-1, y-1

empty_paths = False
for _ in range(k):
    available_paths = bfs(x,y)
    if len(available_paths) == 0:
        empty_paths = True
        break
    available_paths = sorted(available_paths, key=lambda x:(-x[2],x[0],x[1]))
    x, y = available_paths[0][0], available_paths[0][1]

if empty_paths == True:
    print(x+1,y+1)
else:
    print(available_paths[0][0]+1, available_paths[0][1]+1)