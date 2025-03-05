n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))  # 10000개 어레이 생성할 필요 없이 pos 자체를 값으로 해서 리스트에 넣음
    c.append(char)

# 카운팅 어레이
# grid = [0 for _ in range(10001)]

# for _ in range(n):
#     num, c = input().split()
#     if c == 'G':
#         grid[int(num)] = 1
#     else:
#         grid[int(num)] = 2

# ans = 0

# for i in range(1,len(grid)-k+1): # 구간의 시작점
#     score = sum(grid[i:i+k+1])
#     ans = max(score, ans)
# print(ans)

# 모든 구간
ans = 0
for start in range(1, 10000-k+1):
    end = start + k
    # 구간 [start, end] 내의 G, H 개수 세서 점수 구하기
    score = 0
    # 모든 G,H에 대해 구간 내 있는지 확인
    for i in range(n):
        if start <= x[i] <= end:
            if c[i] == 'G':
                score += 1
            else:
                score += 2
    ans =   max(ans, score) 

print(ans)