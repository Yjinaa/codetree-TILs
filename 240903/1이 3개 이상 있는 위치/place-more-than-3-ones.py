n = int(input())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

dirs = [(0,1), (1,0), (0,-1), (-1,0)]

answer = 0

for row in range(len(grid)):
    for col in range(len(grid[0])):
        cnt = 0
        for direction in dirs:
            nx, ny = row + direction[0], col + direction[1]
            if 0<= nx < len(grid) and 0<= ny < len(grid[0]) and grid[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            answer += 1

print(answer)