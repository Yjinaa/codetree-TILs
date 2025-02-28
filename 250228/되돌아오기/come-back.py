N = int(input())

# Please write your code here.

x, y = 0, 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

directions = {'E':0, 'S':1, 'W':2, 'N':3}
sec = 0

for _ in range(N):
    d, dist = input().split()
    dist = int(dist)
    for i in range(dist):
        x += dx[directions[d]]
        y += dy[directions[d]]
        sec += 1
        if x == 0 and y == 0:
            print(sec)
            exit()

print(-1)
