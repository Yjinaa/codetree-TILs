R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.

## bfs 풀이
# queue = []

# row, col, jumped = 0, 0, 0
# queue.append((row,col, jumped))
# cnt = 0

# while queue:
#     row, col, jumped = queue.pop()
#     for i in range(row+1, R):
#         for j in range(col+1, C):
#             if i == R-1 and j == C-1:
#                 if jumped == 2 and grid[row][col] != grid[i][j]:
#                     cnt += 1
#                 continue
#             if grid[row][col] != grid[i][j]:
#                 queue.append((i,j,jumped+1))
# print(cnt)

## 완탐 풀이 - 점프 2번이라고 해서 가능
cnt = 0

for row in range(1, R):
    for col in range(1, C):
        for i in range(row+1, R-1):
            for j in range(col+1, C-1):
               if grid[0][0] != grid[row][col] and grid[row][col] != grid[i][j] and grid[i][j] != grid[R-1][C-1]:
                cnt += 1 
print(cnt)