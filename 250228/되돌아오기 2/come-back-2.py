commands = list(input())

# Please write your code here.

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x, y = 0, 0

cur_dir = 3

sec = 0

for command in commands:
    sec += 1
    if command == 'L':
        cur_dir = (cur_dir+3)%4
    elif command == 'R':
        cur_dir = (cur_dir+1)%4
    elif command == 'F':
        x, y = x + dx[cur_dir], y+dy[cur_dir]
        if x == 0 and y == 0:
            print(sec)
            exit()
print(-1)
