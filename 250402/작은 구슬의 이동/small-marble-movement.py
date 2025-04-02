n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)
r, c = r-1, c-1

# Please write your code here.

dx = [0,-1,1,0]
dy = [1,0,0,-1]

DIR_MAP = {'L':3, 'R':0, 'U':1, 'D':2}
d = DIR_MAP[d]

for i in range(t):
    nr, nc = r + dx[d], c + dy[d]
    if not(0 <= nr < n and 0 <= nc < n):
        d = 3-d
    else:
        r, c = nr, nc

print(r+1, c+1)