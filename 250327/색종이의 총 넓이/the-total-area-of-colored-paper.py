n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.

grid = [[0 for _ in range(210)] for _ in range(210)]

for i in range(n):
    for row in range(x[i]+100,x[i]+100+8):
        for col in range(y[i]+100,y[i]+100+8):
            grid[row][col] = 1

tot_sum = 0
for row in grid:
    tot_sum += sum(row)

print(tot_sum)