n,m = map(int, input().split())

num = 1

# 0,0
# 0,1   1,0
# 0,2   1,1    2,0
# 1,2   2,1
# 2,2

0,1,2


# 0,3   1,2    2,1    3,0

# 0,0
# 0,1   1,0
# 1,1   2,0
# 2,1   3,0
# 3,1



arr = [[0 for _ in range(m)] for _ in range(n)]


for j in range(m): # 0,0
    i=0
    while j != -1:
        arr[i][j] = num
        i += 1
        j -= 1
        num += 1

for i in range(1,n):
    j = m-1
    while j != -1 and i < n:
        arr[i][j] = num
        i += 1
        j -= 1
        num += 1

for _arr in arr:
    print(*_arr)