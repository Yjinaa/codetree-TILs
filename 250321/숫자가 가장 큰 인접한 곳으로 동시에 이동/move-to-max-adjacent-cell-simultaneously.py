n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
marbles = [(r-1,c-1) for r,c in marbles]

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
        max_num = 0
        r, c = marbles[i]
        # print(r,c,a[r][c])
        for j in range(4):
            nr, nc = r + dx[j], c + dy[j]
            if 0 <= nr < n and 0 <= nc < n:
                if a[nr][nc] > max_num:
                    _r,_c = nr, nc
                    max_num = a[nr][nc]
                    # print(max_num)
        r,c = _r,_c
        loc[r][c] += 1
        # for p in loc:
        #     print(*p)
        # print()
    marbles = get_marbles(loc)

print(len(marbles))

# 1. 최대값으로 갱신하는 로직 빼먹음 (_r, _c 사용하지 않고 r,c = nr,nc로 갱신하는 바람에 옮길 때마다 r,c가 갱신되어 기존 기준 좌표가 흔들리게 됨)
# 2. 최대값이 더이상 없어 구슬이 움직이지 않을 경우 처리 안함 > 움직이지 않았는데 그냥 마지막 위치에 +1 해버리니까 2가 돼서 터짐 > moved = True/False 플래그 활용으로 움직였을 때만 새로운 위치, 안움직였을 경우 기존 r,c에 +1
# 3. r,c가 아니라 r,c의 인접 4개 값 중 최대값으로 움직이는건데 a[r][c]보다 클 때만 움직이려고 함.. a[r][c]는 고려대상이 아님 아예 걍 4군데중 최대값으로 이동만 하면 되는거였음