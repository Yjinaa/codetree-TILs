import sys
board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

found = False
for row in range(len(board)):
    for col in range(len(board[0])):
        if board[row][col] != 0:
            for i in range(8):
                cx, cy, cnt = row, col, 1
                while True:
                    nx, ny = cx + dx[i], cy + dy[i]
                    if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                        if board[cx][cy] == board[nx][ny]:
                            cnt += 1
                            cx = nx
                            cy = ny
                        else:
                            break
                    else:
                        break

                    if cnt == 5:
                        print(board[row][col])
                        print(row + 2 * dx[i] + 1, col + 2 * dy[i] + 1)
                        sys.exit()
                            
print(0)