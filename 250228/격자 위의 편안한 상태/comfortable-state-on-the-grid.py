n, m = map(int, input().split())
grid = [[0 for _ in range(n)] for _ in range(n)]

# Please write your code here.

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(m):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    grid[r][c] = 1
    colored = 0
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc]:
            colored += 1
    if colored == 3:
        print(1)
    else:
        print(0)
