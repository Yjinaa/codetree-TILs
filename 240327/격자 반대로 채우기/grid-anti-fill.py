n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]

num = 1

# # n-1이 짝수면 짝수번째 줄마다 거꾸로, 홀수면 홀수번째 줄마다 거꾸로

# if n-1 % 2 == 0:
#     for i in range(n-1,-1,-1):
#         if i % 2 == 0:
#             for j in range(n-1, -1, -1):
#                 arr[j][i] = num
#                 num += 1
#         else:
#             for j in range(n):
#                 arr[j][i] = num
#                 num += 1
# else:
#     for i in range(n-1,-1,-1):
#         if i % 2 == 1:
#             for j in range(n-1,-1,-1):
#                 arr[j][i] = num
#                 num += 1
#         else:
#             for j in range(n):
#                 arr[j][i] = num
#                 num += 1

direction = 'reverse'
for i in range(n-1,-1,-1):
    if direction == 'reverse':
        for j in range(n-1,-1,-1):
            arr[j][i] = num
            num += 1
        direction = 'normal'
    else:
        for j in range(n):
            arr[j][i] = num
            num += 1
        direction = 'reverse'


        


for _arr in arr:
    print(*_arr)