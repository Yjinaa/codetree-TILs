N, C, G, H = map(int, input().split())
ranges = sorted([tuple(map(int, input().split())) for _ in range(N)])
start = ranges[0][0]
end = ranges[-1][1]

# Please write your code here.

def get_workload(ta,tb,temp):
    if temp < ta:
        return C
    elif ta <= temp <= tb:
        return G
    else:
        return H

ans = 0
for temp in range(start, end+1):
    workload = 0
    for machine in ranges:
        ta, tb = machine
        workload += get_workload(ta,tb,temp)
    ans = max(ans, workload)
print(ans)

# ================
# # 강의 답안
# ================

# # get_workload 함수는 똑같음

# ans = 0
# # 1에서 1000까지 모든 범위에 대해 탐색
# for t in range(0,1001):
#     total_output = 0
#     # N개의 장비에 대해 각각 작업량 계산하여 누적

#     # =======================
#     # 1. 기존 접근방식
#     # =======================

#     for i in range(N):
#         total_output += output(t, ranges[i][0], ranges[i][1])
    
#     # ========================
#     # 2. 좀더 pythonic
#     # ========================
#     total_output = sum([
#         output(t, T_a, T_b)
#         for T_a, T_b in ranges
#     ])

    
#     ans = max(ans, total_output)

# print(ans)


