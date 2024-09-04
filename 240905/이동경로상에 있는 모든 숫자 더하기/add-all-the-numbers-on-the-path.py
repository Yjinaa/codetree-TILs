n, t = map(int, input().split())
directions = list(input())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = 3
mid = n//2
x, y = mid, mid

ans = grid[mid][mid]

for direction in directions:
    if direction == 'L':
        d = (d+3)%4
    elif direction == 'R':
        d = (d+1)%4
    else:
        nx, ny = x + dx[d], y+dy[d]
        if not(0 <= nx < n and 0 <= ny < n):
            continue
        ans += grid[nx][ny]
        x, y = nx, ny

print(ans)