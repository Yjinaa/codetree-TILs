n, t = map(int, input().split())
r, c, d = input().split()

dx = [0,1,-1,0]
dy = [1,0,0,-1]

x,y = int(r), int(c)

dir_map = {"U":2, "D":1, "R":0,"L":3}

dir_num = dir_map[d]

def in_range(x,y):
    return 1<=x and x<n and 1<=y and y<n

for time in range(t):
    nx,ny = x+dx[dir_num], y+dy[dir_num]
    if in_range(nx,ny):
        x,y = nx, ny
    else:
        dir_num = 3-dir_num

print(x,y)