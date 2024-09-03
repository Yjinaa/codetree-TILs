n, t = map(int, input().split())
r, c, d = input().split()

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

dir_map = {'U':2, 'R':0, 'L':3, 'D':1}

d = dir_map[d]
r, c = int(r), int(c)

for i in range(t):
    nr, nc = r + dx[d], c + dy[d]
    if 1 <= nr < n and 1 <= nc < n:
        r, c = nr, nc
    else:
        d = 3 - d

print(r, c)