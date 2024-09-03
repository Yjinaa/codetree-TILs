n, m = map(int, input().split())

grid = [[0]*n for _ in range(n)]

dirs = [(0,1), (1, 0), (0, -1), (-1, 0)]

for i in range(m):
    r, c = map(int, input().split())
    r = r-1
    c = c-1
    grid[r][c] = 1
    cnt = 0
    for direction in dirs:
        nr, nc = r + direction[0], c + direction[1]
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)