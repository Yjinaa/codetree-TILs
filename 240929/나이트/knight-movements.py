from collections import deque
n = int(input())

grid = [[0]*n for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dxs = [-1,-2,-2,-1,1,2,2,1]
dys = [-2,-1,1,2,2,1,-1,-2]

def bfs():
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != True:
                queue.append((nx,ny))
                grid[nx][ny] = grid[x][y] + 1
                visited[nx][ny] = True
                if nx == r2 and ny == c2:
                    return

r1, c1, r2, c2 = map(int, input().split())
r1, c1, r2, c2  = r1-1, c1-1, r2-1, c2-1


queue = deque([(r1,c1)])
bfs()
if visited[r2][c2] == True:
    print(grid[r2][c2])
else:
    print(-1)