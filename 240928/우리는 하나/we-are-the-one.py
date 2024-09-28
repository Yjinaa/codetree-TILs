from collections import deque
from itertools import combinations

n, k, u, d = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
# visited = [[False] * n for _ in range(n)]

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

countries = [(i,j) for i in range(n) for j in range(n)]
combs = list(combinations(countries, k))

def bfs(visited):
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != True and u <= abs(grid[nx][ny]-grid[x][y]) <= d:
                 queue.append((nx,ny))
                 visited[nx][ny] = True
    return visited

max_countries = 0
for comb in combs:
    visited = [[False]*n for _ in range(n)]
    for i in range(k):
        x, y = comb[i]
        queue = deque([(x,y)])
        visited[x][y] = True
        visited = bfs(visited)
    total_countries = sum([sum(row) for row in visited])
    if total_countries > max_countries:
        max_countries = total_countries

print(max_countries)