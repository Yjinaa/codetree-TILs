# Please write your code here.

ans = [[0 for i in range(2000)] for _ in range(2000)]

for _ in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 1000
    x2 += 1000
    y1 += 1000
    y2 += 1000

    for x in range(x1, x2):
        for y in range(y1, y2):
            
            ans[x][y] = 1


x1, y1, x2, y2 = map(int, input().split())
x1 += 1000
x2 += 1000
y1 += 1000
y2 += 1000

for x in range(x1, x2):
    for y in range(y1, y2):
        ans[x][y] -= 1

cnt = 0
for i in range(2000):
    for j in range(2000):
        if ans[i][j] == 1:
            cnt += 1

print(cnt)