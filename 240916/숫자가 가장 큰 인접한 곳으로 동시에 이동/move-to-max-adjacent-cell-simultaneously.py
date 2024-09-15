n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
marbles = []
for i in range(m):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    marbles.append((r,c))

# 구슬 위치를 가리키는 m_grid
m_grid = [[0]*n for i in range(n)]
for marble in marbles:
    x, y = marble
    m_grid[x][y] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, next_move): # 상,하, 좌, 우 중 가장 큰 곳으로 이동하는 함수
    max_val = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > max_val:
            max_val = grid[nx][ny]
            fin_x, fin_y = nx, ny
    # print(f'before:{x,y}, after:{fin_x,fin_y}, max_val:{max_val}')
    next_move[fin_x][fin_y] += 1

def eliminate_marbles(m_grid):
    for k in range(n):
        for l in range(n):
            if next_move[k][l] >= 2:
                next_move[k][l] = 0

sec = 1
while sec <= t:
    next_move = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if m_grid[r][c] == 1:
                # print(sec,'sec')
                move(r, c, next_move)

    eliminate_marbles(next_move)

    for row in range(n):
        for col in range(n):
            m_grid[row][col] = next_move[row][col]
    # print(sec, m_grid)
    
    sec += 1

total_sum = 0
for row in m_grid:
    total_sum += sum(row)

print(total_sum)