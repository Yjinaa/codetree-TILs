# 12:21
n, m, r, c = map(int, input().split())
grid = [[0]*n for _ in range(n)]
x, y = r-1, c-1
dirs = list(input().split())

# 마주보는 면 끼리 적힌 숫자 합 = 7
# 숫자는 덮어씌워질 수 있음

d = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}

# 아래로 계속 굴리면 6, 2, 1, 5 반복, 왼쪽으로 계속 굴리면 6, 4, 1, 3 반복
# 현재 밑 면을 기준으로 당장 굴릴 수 있는 방향은 = 전개도로 봤을 때 상하좌우
# 즉 6을 기준으로는 시계방향으로 3 2 4 5
# 4를 기준으로는 6 2 1 5
# 2를 기준으로는 6 3 1 4
# 아 그런데 이렇게 하면 안되겠다.. 똑같이 6이 있어도 오른쪽에 3이 올때가 있고 5가 올때가 있네 5가 오면 5 3 2 4네 아 3이 있으면 3245 5가 있으면 5324 2가 있으면 2453
# 아하. 일단 밑면 기준으로 7에서 뺀 수(=1)는 다음 밑면이 될 수 없음.

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

DIR_MAP = {'L':2, 'R':0, 'D':1, 'U':3}

def move(x, y, direction):
    nx, ny = x + dx[direction], y + dy[direction]
    if 0 <= nx < n and 0 <= ny < n:
        x, y = nx, ny
    return x, y

def change_dice(up, front, right, direction):
    if direction == 2:
        return right, front, 7-up
    elif direction == 0:
        return 7-right, front, up
    elif direction == 3:
        return front, 7-up, right
    elif direction == 1:
        return 7-front, up, right

def simulate(x, y, dirs, up, front, right):
    for i in range(len(dirs)):
        direction = DIR_MAP[dirs[i]]
        x, y = move(x, y, direction)
        up, front, right = change_dice(up, front, right, direction)
        bottom = 7-up
        grid[x][y] = bottom

up, front, right = 1, 2, 3
grid[x][y] = 7-up
simulate(x, y, dirs, up, front, right)

total_sum = 0
for row in grid:
    total_sum += sum(row)

print(total_sum)


# if direction == '2':
#             x, y = move(x, y, direction)
#             up, front, right = right, front, 7-up
#         elif direction == '0':
#             x, y = move(x, y, direction)
#             up, front, right = 7-right, front, up
#         elif direction == '3':
#             x, y = move(x, y, direction)
#             up, front, right = front, 7-up, right
#         elif direction == '1':
#             x, y = move(x, y, direction)
#             up, front, right = 7-front, up, right