n, m, q = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

r, d = input().split()
r = int(r) - 1 # 1 <= r이므로 index로 교체

if q == 0:
    for row in grid:
        print(*row)
        exit()

def shift_left(grid, r):
    # r번째 행을 왼쪽으로 shift
    temp = grid[r][0]
    for i in range(0,m-1):
        grid[r][i] = grid[r][i+1]
    grid[r][m-1] = temp


def shift_right(grid, r):
    # r번째 행을 오른쪽으로 shift
    temp = grid[r][m-1]
    for i in range(m-1,0,-1):
        grid[r][i] = grid[r][i-1]
    grid[r][0] = temp


def has_common_elements(list1, list2):
    # n행과 인접한 행에 같은 원소가 있는지 조사
    # 위/아래 방향에 따라 각각 선언해줘야 할듯 (한번에 할 수도 있나?)
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            return True
        else:
            continue
    return False



for nth in range(q):
    swell = -1
    if d == 'L': # 처음 바람 방향이 L일 경우
        shift_right(grid, r)
        swell_first = 'r'
        swell = 'r'
    elif d == 'R': # 처음 바람 방향이 R일 경우
        shift_left(grid, r)
        swell_first = 'l'
        swell = 'l'
    # 여파 계산
    for i in range(r,0,-1): # upper bound
        if has_common_elements(grid[i], grid[i-1]): # 윗 행과 같은 원소가 있다면
            if swell == 'r':
                shift_left(grid, i-1)
                swell = 'l'
            elif swell == 'l':
                shift_right(grid, i-1)
                swell = 'r'
    swell = swell_first
    for i in range(r, n-1): # lower bound
        if has_common_elements(grid[i], grid[i+1]):
            if swell == 'r':
                shift_left(grid, i+1)
                swell = 'l'
            elif swell == 'l':
                shift_right(grid, i+1)
                swell = 'r'

for row in grid:
    print(*row)