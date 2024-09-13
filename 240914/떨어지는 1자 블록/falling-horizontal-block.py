n, m, k = map(int, input().split())
k = k-1

grid = [list(map(int, input().split())) for _ in range(n)]

def simulate():
    while True:
        is_touched = False
        for row in range(n):
            for col in range(k, k+m):
                # print(f'grid[{row}][{col}] = {grid[row][col]}')
                if grid[row][col] == 0 and row != n-1:
                    continue
                elif row == n-1:
                    grid[row][k:k+m] = [1] * m
                    return grid
                else:
                    grid[row-1][k:k+m] = [1] * m
                    return grid
                
grid = simulate()
for row in grid:
    print(*row)