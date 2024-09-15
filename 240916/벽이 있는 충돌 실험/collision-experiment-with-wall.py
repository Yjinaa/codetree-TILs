T = int(input())
DIR_MAP = {'R':0, 'D':1, 'L':2, 'U':3}
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 서로 부딪히지 않을 조건
# 어차피 방향이 일직선으로만 바뀌므로 n*2번 이상 구슬이 사라지지 않았을 때 개수 세서 리턴하면 된다

def move(r,c,d,switched_grid):
    nx, ny = r + dx[d], c + dy[d]
    if 0 <= nx < n and 0 <= ny < n:
        switched_grid[nx][ny][0] += 1
        switched_grid[nx][ny][1] = d
    else:
        d = (d+2)%4
        switched_grid[r][c][0] += 1
        switched_grid[r][c][1] = d

def eliminate_marbles(switched_grid, exploded):
    for row in range(n):
        for col in range(n):
            if switched_grid[row][col][0] >= 2:
                exploded = True
                switched_grid[row][col][0] = 0
                switched_grid[row][col][1] = '*'
                return exploded
    return exploded

for i in range(T):
    n, m = map(int, input().split())
    marbles = [(int(x)-1,int(y)-1,DIR_MAP[d]) for x,y,d in [input().split() for _ in range(m)]]
    grid = [[[0,-1] for _ in range(n)] for _ in range(n)]
    dirs = [[0]*n for _ in range(n)]
    for marble in marbles:
        x, y, d = marble
        grid[x][y][0] = 1
        grid[x][y][1] = d
    
    switched_num = 0
    while True:
        # print(switched_num)
        if switched_num >= n+2:
            break
        switched_grid = [[[0,-1] for _ in range(n)] for _ in range(n)]
        switched_dirs = [[0]*n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                if grid[r][c][0] == 1:
                    move(r,c,grid[r][c][1], switched_grid)
        # print(switched_grid)
                
        exploded = False
        exploded = eliminate_marbles(switched_grid, exploded)
        if exploded == False:
            switched_num +=1
        else:
            switched_num = 0
        
        for a in range(n):
            for b in range(n):
                grid[a][b][0] = switched_grid[a][b][0]
                grid[a][b][1] = switched_grid[a][b][1]

    total_sum = 0
    for row in grid:
        row = [x[0] for x in row]
        total_sum += sum(row)
    print(total_sum)