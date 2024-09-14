n, m, r, c = map(int, input().split())
x, y = r-1, c-1
grid = [[0]*n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

grid[x][y] = 1


def search_and_put_bomb(grid, t):# 격자판을 돌며 폭탄이 있는지 판단, 있으면 새 폭탄을 던지는 new_bomb 실행
    temp = [[0]*n for _ in range(n)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                temp[i][j] = 1
                distance = 2**(t-1)
                for k in range(4):
                    nx, ny = x + distance*dx[k], y + distance*dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        temp[nx][ny] = 1
    return temp



def simulate(grid, t=1): 
    while t <= m:
        grid = search_and_put_bomb(grid, t)
        t += 1
    return grid

grid = simulate(grid)

total_sum = 0
for row in grid:
    total_sum += sum(row)

print(total_sum)