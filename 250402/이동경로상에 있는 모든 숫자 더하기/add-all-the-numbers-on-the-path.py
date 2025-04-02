n, t = map(int, input().split())
ds = input()
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = n//2, n//2

cur_sum = grid[x][y]
cur_d = 3
for i in range(t):
    if ds[i] == 'F':
        nx, ny = x + dx[cur_d], y + dy[cur_d]
        if 0 <= nx < n and 0 <= ny < n:
            x, y = nx, ny
            cur_sum += grid[x][y]
        else:
            continue
    else:
        cur_d = (cur_d+3)%4 if ds[i] == 'L' else (cur_d + 1)%4

print(cur_sum)
    