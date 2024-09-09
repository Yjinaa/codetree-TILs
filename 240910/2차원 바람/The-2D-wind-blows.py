import copy
n, m, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def cal_avg(r,c, shifted_grid):
    # r,c에서 기존 직사각형의 4방향의 평균값을 구하는 함수
    # put_avg에서 grid에 새 값을 넣어줌으로 인해 계산값이 바뀌면 안되니까 계산용 동일 grid를 따로 만들어 줌. (근데 반드시 시계방향으로 바뀌고 난 뒤의 그리드여야 함)
    sum = shifted_grid[r][c]
    num = 5
    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            sum += shifted_grid[nx][ny]
        else:
            num -= 1
    return sum//num

def put_avg(r1, c1, r2, c2, shifted_grid):
    # 직사각형 영역 내 요소들의 값을 바꾸는 함수
    for row in range(r1, r2+1):
        for col in range(c1, c2+1):
            avg = cal_avg(row, col, shifted_grid)
            grid[row][col] = avg

def shift(r1,c1,r2,c2):
    # 시계방향으로 한 칸씩 shift하는 함수
    # 직사각형 윗변
    temp = grid[r1].pop(c2)
    grid[r1].insert(c1, '*') # 왼쪽변 원소가 올라올 자리를 주면서 오른쪽으로 shift
    # 직사각형 왼쪽 변
    for row in range(r1,r2):
        grid[row][c1] = grid[row+1][c1]
    # 직사각형 아랫변
    grid[r2].pop(c1)
    grid[r2].insert(c2, '*')
    # 직사각형 오른쪽 변
    for row in range(r2,r1,-1):
        grid[row][c2] = grid[row-1][c2]
    grid[r1+1][c2] = temp
    shifted_grid = copy.deepcopy(grid)
    return shifted_grid

def simulate(q):
    r1, c1, r2, c2 = map(int, input().split())
    # 인덱스 범위로 교체
    r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
    if q == 0:
        for row in grid:
            print(*row)
        return
    for i in range(q):
        shifted_grid = shift(r1, c1, r2, c2)
        put_avg(r1, c1, r2, c2, shifted_grid)
    for row in grid:
        print(*row)
    return

simulate(q)