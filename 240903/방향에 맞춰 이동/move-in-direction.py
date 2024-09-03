n = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
dir_map = {'E':0, 'W':1, 'S':2, 'N':3}

x,y = 0,0

for i in range(n):
    direction, distance = input().split()
    direction = dir_map[direction]
    x = x + dx[direction] * int(distance)
    y = y + dy[direction] * int(distance)

print(x,y)