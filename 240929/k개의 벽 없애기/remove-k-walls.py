from collections import deque
from itertools import combinations
import sys

n, k = map(int, input().split())

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

ks = [(i,j) for i in range(n) for j in range(n) if grid[i][j] == 1]
combs = list(combinations(ks,k))

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1

def bfs():
    time = 0
    while queue:
        x, y, time = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != True and _grid[nx][ny] != 1:
                queue.append((nx, ny, time+1))
                visited[nx][ny] = True
                if nx == r2 and ny == c2:
                    return time+1
    return -1

min_time = sys.maxsize
for comb in combs:
    _grid = [row[:] for row in grid]
    visited = [[False]*n for _ in range(n)]
    for i in range(k):
        x,y = comb[i][0],comb[i][1]
        _grid[x][y] = 0
    queue = deque([(r1, c1, 0)])
    visited[r1][c1] = True
    time = bfs()
    if time == -1:
        continue
    min_time = min(min_time, time)

if min_time == sys.maxsize:
    print(-1)
else:
    print(min_time)