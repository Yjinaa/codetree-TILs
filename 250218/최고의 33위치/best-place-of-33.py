n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!

def get_coins(grid, row_s, col_s, row_e, col_e):
    coins = 0
    for row in range(row_s, row_e+1):
        for col in range(col_s, col_e+1):
            coins += grid[row][col]
    return coins    



max_coins = 0
for row in range(n):
    for col in range(n):
        if (col+2 >= n) or row + 2 >= n:
            continue
        else:
            coins = get_coins(grid, row, col, row+2, col+2)
            if max_coins < coins:
                max_coins = coins
            
print(max_coins)