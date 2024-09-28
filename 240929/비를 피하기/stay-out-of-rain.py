from collections import deque

n, h, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def bfs(visited, i, j):
    while queue:
        x, y, distance= queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != True and grid[nx][ny] !=1:
                queue.append((nx, ny, distance+1))
                visited[nx][ny] = True
                if grid[nx][ny] == 3:
                    if ans[i][j] == 0:
                        ans[i][j] = distance + 1
                    else:
                        ans[i][j] = min(ans[i][j], distance+1)
                    return
    ans[i][j] = -1
    return



ans = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            visited = [[False]*n for _ in range(n)]
            i_ans = [[0]*n for _ in range(n)]
            queue = deque([(i,j,0)])
            visited[i][j] = True
            distance = bfs(visited, i, j)

for row in ans:
    print(*row)