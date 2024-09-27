from collections import deque

n, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
check_board = [[0]*n for _ in range(n)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def bfs():
    available_paths = 1
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != True and grid[nx][ny] != 1:
                queue.append((nx,ny))
                visited[nx][ny] = True
                check_board[nx][ny] = 1
                available_paths += 1
    return available_paths

total_paths = 0
for _ in range(k):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    check_board[x][y] = 1
    queue = deque([(x,y)])
    available_paths = bfs()
    total_paths += available_paths

print(sum(sum(row) for row in check_board))