n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]

num = 1

for i in range(n):

    for j in range(n):
        arr[j][i] = num
        num += 1
    # else:
    #     for j in range(n-1,-1,-1):
    #         arr[j][i] = num
    #         num += 1

for _arr in arr:
    print(*_arr)