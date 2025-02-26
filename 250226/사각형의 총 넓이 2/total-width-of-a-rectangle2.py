n = int(input())

# Please write your code here.

ans = [[0 for i in range(201)] for _ in range(201)] 


for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    # x1 += 100
    # y1 += 100
    # x2 += 100
    # y2 += 100 

    for x in range(x1, x2):  # 격자가 아니고 구간이기 때문에 +1 하지 않음
        for y in range(y1, y2):
            ans[x][y] = 1

tot_sum = 0
for row in ans:
    tot_sum += sum(row)
print(tot_sum)


