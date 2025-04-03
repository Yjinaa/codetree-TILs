n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_cnt = 0

for row in range(n):
    for col in range(n-3+1):
        cur_cnt = 0
        for i in range(col, col+3):
            if grid[row][i] == 1:
                cur_cnt += 1
        max_cnt = max(cur_cnt, max_cnt)

print(max_cnt)