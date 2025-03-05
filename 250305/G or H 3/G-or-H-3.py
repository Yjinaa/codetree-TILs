n, k = map(int, input().split())
# l = sorted([tuple(input().split()) for _ in range(n)]) # 최대 거리 어떻게 구함?

grid = [0 for _ in range(10001)]

for _ in range(n):
    num, c = input().split()
    if c == 'G':
        grid[int(num)] = 1
    else:
        grid[int(num)] = 2

ans = 0

for i in range(1,len(grid)-k+1): # 구간의 시작점
    score = sum(grid[i:i+k+1])
    ans = max(score, ans)
print(ans)