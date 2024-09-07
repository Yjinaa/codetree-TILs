n = int(input())
grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

def count_coins(grid, row_s, row_e, col_s, col_e):
    coins = 0
    for row in range(row_s, row_e + 1):
        for col in range(col_s, col_e + 1):
            if grid[row][col] == 1:
                coins += 1
            else:
                continue
    return coins

max_coins = 0
for row in range(n):
    for col in range(n):
        if col + 2 > n-1 or row + 2 > n-1:
            continue
        else:

            coins = count_coins(grid, row, row+2, col, col+2)
            if coins > max_coins:
                max_coins = coins

print(max_coins)