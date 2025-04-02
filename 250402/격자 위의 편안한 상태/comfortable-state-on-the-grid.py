n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]
grid = [[0 for _ in range(n)] for _ in range(n)]

# Please write your code here.

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

tot_cnt = 0
for point in points:
    row, col = point
    row, col = row-1, col-1
    grid[row][col] = 1
    cur_cnt = 0
    for i in range(4):
        nx, ny = row + dx[i], col + dy[i]
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
            cur_cnt += 1
    if cur_cnt == 3:
        print(1)
    else:
        print(0)