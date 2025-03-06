import sys

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

def get_distance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

# ans = 0
# for i in range(1,n): # i: 제외할 체크포인트, 1과 N 제외이므로 -1,n
#     distance = 0
#     for j in range(n-1): # 제외한 체크포인트 빼고 다 방문
#         if j == i:
#             continue
#         distance += get_distance(x[j],y[j],x[j+1],y[j+1])  # 이렇게 하면 제외한 체크포인트도 +1에 걸리면 dist를 구해버리게 됨
#     ans = max(distance, ans)

# print(ans)

# >> 현재위치를 저장해놓고 방문할 체크포인트 <> 현재 위치 간 거리를 누적하자
ans = sys.maxsize
for i in range(1,n-1): # i: 제외할 체크포인트, 1과 N 제외이므로 range(1, n-1)
    distance = 0
    cur_x, cur_y = x[0], y[0] # 현재 위치 추가
    for j in range(1, n): # 제외한 체크포인트 빼고 다 방문
        if j == i:
            continue
        distance += get_distance(cur_x, cur_y, x[j], y[j])
        cur_x, cur_y = x[j], y[j]
    ans = min(distance, ans)

print(ans)