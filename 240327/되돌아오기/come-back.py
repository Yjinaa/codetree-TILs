n = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

DIR_MAP = {"E":0, "S":1,"W":2,"N":3}

x,y = 0,0

time = 0
for i in range(n):
    direction, distance = input().split()
    direction = DIR_MAP[direction]
    for go in range(int(distance)):
        x, y = x + dx[direction], y + dy[direction]
        time += 1
        if x == 0 and y == 0:
            print(time)
            exit()

print(-1)