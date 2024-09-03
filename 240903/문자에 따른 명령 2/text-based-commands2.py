dirs = list(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x, y = 0, 0
cur_dir = 3

for direction in dirs:
    if direction == 'L':
        cur_dir = (cur_dir + 3) % 4
    elif direction == 'R':
        cur_dir = (cur_dir + 1) % 4
    else:
        x, y = x + dx[cur_dir], y + dy[cur_dir]


print(x, y)