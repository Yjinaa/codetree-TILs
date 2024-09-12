from collections import defaultdict
n,m = map(int, input().split())

b = [int(input()) for _ in range(n)]

temp = []
num_cnt = 1

# for i in range(len(b)-1):
#     while b[i] == b[i+1]:
#         num_cnt += 1
#         print(num_cnt)
#     if num_cnt < m:
#         temp[temp_idx] = b[i]
#         temp_idx += 1

i = 0
while i < len(b)-1:
    num_cnt = 1
    if b[i] == b[i+1]:
        while i < len(b)-1 and b[i] == b[i+1]:
            num_cnt += 1
            i += 1
    if num_cnt < m:
        temp.append(b[i])
    i += 1

if len(temp) == 0:
    print(0)
else:
    print(len(temp))
    for elem in temp:
        print(elem)