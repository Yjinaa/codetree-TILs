n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
def calculate_sum(block_shape, row, col):
    if block_shape == 'L':
        ops = [(0,3),(0,1),(1,2),(2,3)]
        max_val = 0
        for op in ops:
            cal_sum = grid[row][col]
            for j in range(2):
                nx, ny = row + dirs[op[j]][0], col + dirs[op[j]][1]
                if 0 <= nx < n and 0 <= ny < m:
                    cal_sum += grid[nx][ny]
                else:
                    break
            max_val = max(max_val, cal_sum)
        return max_val
    else:
        ops = [(0,2),(1,3)]
        max_val = 0
        for op in ops:
            cal_sum = grid[row][col]
            for j in range(2):
                nx, ny = row + dirs[op[j]][0], col + dirs[op[j]][1]
                if 0 <= nx < n and 0 <= ny < m:
                    cal_sum += grid[nx][ny]
                else:
                    break
            max_val = max(max_val, cal_sum)
        return max_val

block_shape = 'L'
max_val = 0
for row in range(n):
    for col in range(n):
        cal_val = calculate_sum(block_shape, row, col)
        max_val = max(max_val, cal_val)

block_shape = 'else'
for row in range(n):
    for col in range(n):
        cal_val = calculate_sum(block_shape, row, col)
        max_val = max(max_val, cal_val)

print(max_val)