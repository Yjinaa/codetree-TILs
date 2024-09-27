from collections import deque
n,m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def bfs(x,y):
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] != 1 and grid[nx][ny] ==1:
                queue.append((nx,ny))
                visited[nx][ny] = 1

queue = deque([(0,0)])
bfs(0,0)
print(visited[n-1][m-1])