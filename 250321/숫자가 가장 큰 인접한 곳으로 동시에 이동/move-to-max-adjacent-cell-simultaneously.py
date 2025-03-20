n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
marbles = [(r-1,c-1) for r,c in marbles]
loc = [[0 for _ in range(n)] for _ in range(n)]

# Please write your code here.
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def get_marbles(loc):
    temp = []
    for i in range(n):
        for j in range(n):
            if loc[i][j] == 1:
                temp.append((i,j))
            elif loc[i][j] > 1:
                loc[i][j] = 0
    return temp

for k in range(t):
    loc = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(marbles)):
        r, c = marbles[i]
        cur = a[r][c]
        moved = False
        for j in range(4):
            nr, nc = r + dx[j], c + dy[j]
            if 0 <= nr < n and 0 <= nc < n:
                if a[nr][nc] > cur:
                    _r,_c = nr, nc
                    cur = a[nr][nc]
                    moved = True
        if moved == True:
            r,c = _r,_c
        loc[r][c] += 1
    marbles = get_marbles(loc)

print(len(marbles))

# 1. 최대값으로 갱신하는 로직 빼먹음 (_r, _c 사용하지 않고 r,c = nr,nc로 갱신하는 바람에 옮길 때마다 r,c가 갱신되어 기존 기준 좌표가 흔들리게 됨)
# 2. 최대값이 더이상 없어 구슬이 움직이지 않을 경우 처리 안함 > 움직이지 않았는데 그냥 마지막 위치에 +1 해버리니까 2가 돼서 터짐 > moved = True/False 플래그 활용으로 움직였을 때만 새로운 위치, 안움직였을 경우 기존 r,c에 +1
# 3. loc 값을 매번 새로 갱신해서 이전 턴에서 구슬 있던 위치 + 다음 턴에서 구슬 겹칠 경우 생각 안함
# 4. loc 하나에서 다 하려고 함. loc에서만 하면 이전 구슬위치 +1이 되어있는 상태에서 다음 위치까지 +1이 됨 기존 위치와 새 위치 구분 불가
#    new_loc으로 기존위치와 새 위치 구분 필요