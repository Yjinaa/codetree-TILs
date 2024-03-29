n,m = map(int, input().split())

visited = [[0 for _ in range(m)] for _ in range(n)]

x, y = 0,0

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

visited[x][y] = 1

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m

direction = 0

for i in range(2, n*m+1):
    nx, ny = x + dx[direction], y + dy[direction]
    if not in_range(nx, ny) or visited[nx][ny] != 0:
        direction = (direction + 1) % 4
    x,y = x + dx[direction], y + dy[direction]
    visited[x][y] = i


for _visited in visited:
    print(*_visited)