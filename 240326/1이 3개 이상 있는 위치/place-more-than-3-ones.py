n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0<= x < n and 0<= y < n

dxs = [1,0,-1,0]
dys = [0,1,0,-1]

cnts = []

for nx in range(n):
    for ny in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            x, y = nx + dx, ny + dy
            if in_range(x,y) and a[x][y] == 1:
               cnt +=1
        cnts.append(cnt)

print(max(cnts))