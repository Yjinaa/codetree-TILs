n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dx = [0,1,0,-1]
dy = [1,0,-1,0]

tot_cnt = 0
for row in range(n):
    for col in range(n):
        cur_cnt = 0
        for i in range(4):
            nx, ny = row + dx[i], col + dy[i]
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                cur_cnt += 1
        if cur_cnt >= 3:
            tot_cnt += 1

print(tot_cnt)
