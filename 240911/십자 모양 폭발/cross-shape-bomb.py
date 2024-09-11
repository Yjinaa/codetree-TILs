n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

r, c = map(int, input().split())
r, c = r-1, c-1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

bomb_distance = grid[r][c] - 1
grid[r][c] = 0

for i in range(4):
    dr, dc = r, c
    for j in range(bomb_distance):
        nx, ny = dr + dx[i], dc + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            grid[nx][ny] = 0
        dr, dc = nx, ny

temp = [[0]*n for _ in range(n)]
for col in range(n):
    temp_idx = n-1
    zeros = 0
    for row in range(n-1, -1, -1):
        if grid[row][col] != 0:
            temp[temp_idx][col] = grid[row][col]
            temp_idx -= 1
        


for row in temp:
    print(*row)