n = int(input())

grid = [[0 for _ in range(210)] for _ in range(210)]

# Please write your code here.
for _ in range(n):
    x1,y1,x2,y2 = map(int, input().split())
    x1,y1,x2,y2 = x1+100,y1+100,x2+100,y2+100

    for row in range(x1,x2):
        for col in range(y1,y2):
            grid[row][col] = 1

tot_sum = 0
for row in grid:
    tot_sum += sum(row)

print(tot_sum)
