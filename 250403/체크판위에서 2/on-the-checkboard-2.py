R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
queue = []

row, col, jumped = 0, 0, 0
queue.append((row,col, jumped))
cnt = 0

while queue:
    row, col, jumped = queue.pop()
    for i in range(row+1, R):
        for j in range(col+1, C):
            if i == R-1 and j == C-1 and jumped == 2:
                cnt += 1
                continue
            if grid[row][col] != grid[i][j]:
                queue.append((i,j,jumped+1))
print(cnt)