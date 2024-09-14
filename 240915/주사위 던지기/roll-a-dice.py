# 12:21
n, m, r, c = map(int, input().split())
grid = [[0]*n for _ in range(n)]
x, y = r-1, c-1
dirs = list(input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

DIR_MAP = {'L':2, 'R':0, 'D':1, 'U':3}

def move(x, y, direction):
    nx, ny = x + dx[direction], y + dy[direction]
    if 0 <= nx < n and 0 <= ny < n:
        x, y = nx, ny
        return x, y, True
    else:
        return x, y, False

def change_dice(up, front, right, direction):
    if direction == 2:
        return right, front, 7-up
    elif direction == 0:
        return 7-right, front, up
    elif direction == 3:
        return front, 7-up, right
    elif direction == 1:
        return 7-front, up, right

def simulate(x, y, dirs, up, front, right):
    for i in range(len(dirs)):
        direction = DIR_MAP[dirs[i]]
        x, y, moved = move(x, y, direction)
        if moved:
            up, front, right = change_dice(up, front, right, direction)
        bottom = 7-up
        grid[x][y] = bottom

up, front, right = 1, 2, 3
grid[x][y] = 7-up
simulate(x, y, dirs, up, front, right)

total_sum = 0
for row in grid:
    total_sum += sum(row)

print(total_sum)


# if direction == '2':
#             x, y = move(x, y, direction)
#             up, front, right = right, front, 7-up
#         elif direction == '0':
#             x, y = move(x, y, direction)
#             up, front, right = 7-right, front, up
#         elif direction == '3':
#             x, y = move(x, y, direction)
#             up, front, right = front, 7-up, right
#         elif direction == '1':
#             x, y = move(x, y, direction)
#             up, front, right = 7-front, up, right