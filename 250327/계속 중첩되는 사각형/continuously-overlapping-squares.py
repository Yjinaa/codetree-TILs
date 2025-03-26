n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
grid = [[0 for _ in range(201)] for _ in range(201)]
color = -1
for i in range(n):
    for row in range(x1[i]+100, x2[i]+100):
        for col in range(y1[i]+100, y2[i]+100):
            if color == -1:
                grid[row][col] = 1
            else:
                grid[row][col] = 2
    color *= -1 

r, b = 0, 0
for x in range(0,201):
    for y in range(0, 201):
        if grid[x][y] == 1:
            r += 1
        elif grid[x][y] == 2:
            b += 1

print(b)