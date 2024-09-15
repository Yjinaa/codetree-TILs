n,m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

# print(grid)


def move(x,y):
    max_val = 0
    for k in range(8):
        nx, ny = x + dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > max_val:
            max_val = grid[nx][ny]
            fin_x, fin_y = nx, ny
    # print(x,y,max_val)
    grid[x][y], grid[fin_x][fin_y] = grid[fin_x][fin_y], grid[x][y]
    # print(grid)

found = False

for i in range(m):  # m턴 반복
    for j in range(n*n): # 격자 수만큼 반복
        found = False
        for r in range(n):
            if found:
                break
            for c in range(n):
                if grid[r][c] == j+1:
                    # print(r,c,j,'whole')
                    move(r,c)
                    found = True
                    break
                    

for row in grid:
    print(*row)