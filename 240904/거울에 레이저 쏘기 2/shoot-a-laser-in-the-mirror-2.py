n = int(input())
mirrors = []
for _ in range(n):
    row = list(input())
    mirrors.append(row)
k = int(input())

# 방향 맵핑
dir_map = {'E': 0, 'S': 1, 'W': 2, 'N': 3}

# 각 방향에 대한 x, y 이동량
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 레이저 출발 위치 및 방향 설정
if 1 <= k <= n:
    laser = 'S'
    x, y = 0, k - 1
elif n + 1 <= k <= 2 * n:
    laser = 'W'
    x, y = k - n - 1, n - 1
elif 2 * n + 1 <= k <= 3 * n:
    laser = 'N'
    x, y = n - 1, 3 * n - k
else:
    laser = 'E'
    x, y = 4 * n - k, 0

# 레이저 이동 함수
def find_answer(x, y, laser):
    cnt = 0
    while True:
        # 현재 위치가 격자 내에 있는지 확인
        if not (0 <= x < n and 0 <= y < n):
            return cnt

        # 거울에 따라 레이저 방향을 변경
        if mirrors[x][y] == '\\':
            if laser == 'N':
                laser = 'W'
            elif laser == 'E':
                laser = 'S'
            elif laser == 'S':
                laser = 'E'
            elif laser == 'W':
                laser = 'N'
        elif mirrors[x][y] == '/':
            if laser == 'N':
                laser = 'E'
            elif laser == 'E':
                laser = 'N'
            elif laser == 'S':
                laser = 'W'
            elif laser == 'W':
                laser = 'S'

        # 레이저가 이동할 방향에 따라 좌표 업데이트
        d = dir_map[laser]
        x += dx[d]
        y += dy[d]
        cnt += 1

# 정답 출력
print(find_answer(x, y, laser))