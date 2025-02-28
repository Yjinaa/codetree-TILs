n = int(input())


# Please write your code here.

dx = [1,0,-1,0]
dy = [0,-1,0,1]

x, y = 0, 0

for _ in range(n):
    direction, dist = map(str, input().split())
    dist = int(dist)
    if direction == 'N':
        nx, ny = x + dist*dx[3], y + dist*dy[3]
    elif direction == 'W':
        nx, ny = x + dist*dx[2], y + dist*dy[2]
    elif direction == 'E':
        nx, ny = x + dist*dx[0], y + dist*dy[0]
    elif direction == 'S':
        nx, ny = x + dist*dx[1], y + dist*dy[1]
    x, y = nx, ny

print(x,y)