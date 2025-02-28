dirs = list(input())


# Please write your code here.

x, y = 0, 0
cur_dir = 3
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for direction in dirs:
    if direction == 'L':
        cur_dir = (cur_dir+3)%4
    elif direction == 'R':
        cur_dir = (cur_dir+1)%4
    elif direction == 'F':
        x, y = x+dx[cur_dir], y+dy[cur_dir]

print(x,y)

