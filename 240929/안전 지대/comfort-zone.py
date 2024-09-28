# 10:14
n, m = map(int, input().split())
import sys
sys.setrecursionlimit(2500)

grid = [list(map(int, input().split())) for _ in range(n)]
k = 1
max_regions = 0
max_k = 0

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def dfs(x,y):
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] != True and grid2[nx][ny] != 1:
            visited[nx][ny] = True
            dfs(nx,ny)

while True:
    grid2 = [[0]*m for _ in range(n)] # 잠겼는지 여부를 확인할 새 그리드
    visited = [[False] * m for _ in range(n)]
    flooded = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] <= k: # k 보다 작으면
                grid2[i][j] = 1 # 물에 잠김
                flooded += 1
    if flooded == n*m:   # 물에 다 잠기면 종료
        if max_regions == 0:
            max_k = k
        break

    regions = 0  # k에 따른 지역 수 초기화
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid2[i][j] == 0: # 방문 않고 안잠겼을 경우 dfs 탐색
                dfs(i,j)
                regions += 1  # 안전 지역 추가
    if regions > max_regions:
        max_k = k 
        max_regions = regions
    k += 1

print(max_k, max_regions)