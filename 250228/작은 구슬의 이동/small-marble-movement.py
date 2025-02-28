n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

direction = {'R':0, 'D':1, 'L':2, 'U':3}
d = direction[d]

for _ in range(t):
    nx, ny = r + dx[d], c + dy[d]
    if 1 <= nx < n+1 and 1 <= ny < n+1:
        r, c = nx, ny
    else:
        d = (d+2)%4

print(r,c)
