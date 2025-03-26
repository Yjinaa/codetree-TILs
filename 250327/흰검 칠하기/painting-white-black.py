n = int(input())

# Please write your code here.

# 흰색, 검은색, 현재 색 리스트를 따로 만들어 관리
# 현재 색에서는 모두 -1로 초기화, 흰색이면 0 검은색이면 1로 칠하기

w = [0] * 200010
b = [0] * 200010
c = [-1] * 200010

# segments = []

# cur_loc = 0
# for _ in range(n):
#     x, direc = input().split()
#     x = int(x)
    
#     if direc == 'L':
#         left = cur_loc - x + 1
#         right = cur_loc 
#         cur_loc = cur_loc - x + 1
#         color = 'w'
#     else:
#         left = cur_loc 
#         right = cur_loc + x - 1
#         cur_loc = cur_loc + x - 1
#         color = 'b'
#     segments.append([left,right,color])

# for seg in segments:
#     l,r,color = seg[0] + 100000, seg[1] + 100000, seg[2]
#     if color == 'w':
#         for i in range(l,r+1):
#             w[i] += 1
#             c[i] = 0
#     else:
#         for i in range(l,r+1):
#             b[i] += 1
#             c[i] = 1
# w_cnt = 0
# b_cnt = 0
# g_cnt = 0
# for j in range(len(w)):
#     if w[j] >= 2 and b[j] >= 2:
#         g_cnt += 1
#     else:
#         if c[j] == 1:
#             b_cnt += 1
#         elif c[j] == 0:
#             w_cnt += 1

# print(w_cnt, b_cnt, g_cnt)

cur_loc = 100000
for _ in range(n):
    x, direc = input().split()
    x = int(x)
    if direc == 'L':
        for i in range(cur_loc, cur_loc-x, -1):
            w[i] += 1
            c[i] = 0
        cur_loc = cur_loc -x +1
    else:
        for i in range(cur_loc, cur_loc+x):
            b[i] += 1
            c[i] = 1
        cur_loc = cur_loc + x - 1

w_cnt = 0
b_cnt = 0
g_cnt = 0
for j in range(len(w)):
    if w[j] >= 2 and b[j] >= 2:
        g_cnt += 1
    else:
        if c[j] == 1:
            b_cnt += 1
        elif c[j] == 0:
            w_cnt += 1

print(w_cnt, b_cnt, g_cnt)