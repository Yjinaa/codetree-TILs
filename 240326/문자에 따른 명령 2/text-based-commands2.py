directions = input()

x, y = 0,0

dx = [1,0,-1,0]
dy = [0,-1,0,1]

dir_num = 3

for direction in directions:
    if direction == 'L':
        dir_num = (dir_num+3)%4 # 0일 때 3이 되어야 함
    elif direction == 'R':
        dir_num = (dir_num+1)%4 # 3일 때 0이 되어야 함
    else:
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)