n = int(input())

x, y = 0,0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
DIR_MAP = {"N":1, "W":2,"E":0,"S":3}

for i in range(n):
    direction, distance = input().split()
    direction = DIR_MAP[direction]
    x += dx[direction] * int(distance)
    y += dy[direction] * int(distance)

print(x, y)