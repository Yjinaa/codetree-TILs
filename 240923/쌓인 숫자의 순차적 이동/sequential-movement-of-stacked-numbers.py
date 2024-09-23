dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

# 각 칸을 리스트로 관리

n,m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

# 각 칸에 수를 저장할 그리드
targets = list(map(int, input().split()))
cur_grid = [[[] for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        cur_grid[i][j].append(grid[i][j])

# 리스트 내에 타겟이 있으면 어떡하지? index로 찾아도 없다면 오류날텐데
def search_target(target):
    for row in range(n):
        for col in range(n):
            if len(cur_grid[row][col]) != 0:
                for idx, elem in enumerate(cur_grid[row][col]):
                    if elem == target:
                        # print(f'cur_grid[{row}][{col}]={elem},{idx}')
                        return row, col, idx

def move_target(x,y,idx):
    max_val = 0
    for direction in range(8):
        nx,ny = x + dx[direction], y + dy[direction]
        # print(f'[{nx}][{ny}]')
        if 0 <= nx < n and 0 <= ny < n and len(cur_grid[nx][ny])!=0:
            for elem in cur_grid[nx][ny]:
                if elem > max_val:
                    max_val = elem
                    mx,my = nx,ny
                    # print(f'max_val={max_val}, grid[{mx}][{my}]')
    target_list = cur_grid[x][y][idx:]
    cur_grid[x][y] = cur_grid[x][y][:idx]
    # print(cur_grid[x][y], target_list)
    cur_grid[mx][my].extend(target_list)
    # print(cur_grid[mx][my])

for i in range(m):
    target = targets[i]
    # 각 칸에서 주어지는 숫자를 찾는 함수
    x, y, idx = search_target(target)
    move_target(x, y, idx) # 주변에서 가장 큰 숫자로 이동시키는 함수

for r in range(n):
    for c in range(n):
        if len(cur_grid[r][c]) == 0:
            print(None)
        else:
            print(*cur_grid[r][c][::-1])