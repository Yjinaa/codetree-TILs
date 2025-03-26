x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.

grid = [[0 for _ in range(2010)] for _ in range(2010)]
for i in range(2):
    for row in range(x1[i]+1000, x2[i]+1000):
        for col in range(y1[i]+1000, y2[i]+1000):
            grid[row][col] = i+1

min_x = 2010
min_y = 2010
max_x = 0
max_y = 0
for x in range(0,2010):
    for y in range(0,2010):
        if grid[x][y] == 1:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

print((max_x-min_x+1)*(max_y-min_y+1))

