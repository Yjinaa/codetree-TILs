n, r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dx = [-1,1,0,0]
dy = [0,0,-1,1]

r, c = r-1, c-1
ans = [grid[r][c]]

while True:
    moved = False
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if 0 <= nr < n and 0 <= nc < n:
            if grid[nr][nc] > grid[r][c]:
                ans.append(grid[nr][nc])
                r, c = nr, nc
                moved = True
    if moved == False:
        break

print(*ans)