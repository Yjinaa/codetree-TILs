n, r, c = map(int,input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

r, c = r-1, c-1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [grid[r][c]]
while True:
    exist_bigger = True
    num = grid[r][c]
    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > num:
            num = grid[nx][ny]
            r, c = nx, ny
            visited.append(num)
            break
    if (r, c) != (nx, ny):
        exist_bigger = False
    if exist_bigger == False:
        break

print(*visited)