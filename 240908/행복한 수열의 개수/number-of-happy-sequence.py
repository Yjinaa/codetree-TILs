from collections import Counter
from collections import defaultdict

n, m = map(int, input().split())
grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

if len(grid) == 1:
    print(1)
    exit()

happy_r = 0
for row in range(n):
    nums = 1
    for col in range(0, n-1):
        if grid[row][col] == grid[row][col+1]:
            nums += 1
        else:
            nums = 1
        if nums >= m:
            happy_r += 1
            break

happy_c = 0
for col in range(n):
    nums = 1
    for row in range(0,n-1):
        if grid[row][col] == grid[row+1][col]:
            nums += 1
        else:
            nums = 1
        if nums >= m:
            happy_c += 1
            break

print(happy_c + happy_r)