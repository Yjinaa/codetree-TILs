# ========================================================================
# 기본 개념 예제 발전된 풀이 - 이 방식이면 n^2R이 아닌 nR만 투자해도 된다.
# ========================================================================

# n = 5
# segments = [(1, 3), (2, 4), (5, 8), (6, 9), (7, 10)]

# # counting array 선제작 
# count = [0] * 11 # initialize
# for i in range(n):
#     x1, x2 = segments[i]
#     for k in range(x1, x2+1):
#         count[k] += 1

# ans = 100
# for i in range(n):

#     # 제외할 선분 counting array에서 제거
#     x1, x2 = segments[i] # x1, x2: 선분 시작점과 끝점
#     for k in range(x1, x2+1):
#         count[k] -= 1

#     max_cnt = max(count)
#     ans = min(ans, max_cnt)

#     # 제외됐던 것 복구
#     x1, x2 = segments[i] # x1, x2: 선분 시작점과 끝점
#     for k in range(x1, x2+1):
#         count[k] += 1

# print(ans)

# ================
# Problem 풀이
# ================
import sys

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

ans = sys.maxsize
for i in range(n): # 각 점을 제거하는 경우의 수 = n가지, i번 = 제외할 점
    minx, miny = sys.maxsize, sys.maxsize
    maxx, maxy = -sys.maxsize, -sys.maxsize
    for j in range(n):
        if i == j: # 같을때는 continue
            continue
        minx = min(minx, x[j])
        maxx = max(maxx, x[j])
        miny = min(miny, y[j])
        maxy = max(maxy, y[j])

    area = (maxx-minx) * (maxy-miny)
    ans = min(ans, area)
print(ans)

# ====================================
# 가장 pythonic한 방법
# ====================================

# def cal_area_without_i(i):
#     minx = min(x[:i] + x[i+1:])
#     miny = min(y[:i] + y[i+1:])
#     maxx = max(x[:i] + x[i+1:])
#     maxy = max(y[:i] + y[i+1:])
#     area = (maxx-minx) * (maxx-miny)
#     return area
    
