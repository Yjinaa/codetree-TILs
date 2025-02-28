n, m = map(int, input().split())
grid = [[0 for _ in range(n+1)] for _ in range(n+1)]

# Please write your code here.

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(m):
    r, c = map(int, input().split())
    grid[r][c] = 1
    colored = 0
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if 1 <= nr < n+1 and 1 <= nc < n+1 and grid[nr][nc]:
            colored += 1
    if colored >= 3:
        print(1)
    else:
        print(0)
