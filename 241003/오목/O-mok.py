grid = [list(map(int, input().split())) for _ in range(19)]

dxs = [0, 1, 0, -1,-1,1,-1,1]
dys = [1, 0, -1, 0,1,1,-1,-1]

found = False
for i in range(19):
    if found == True:
        break
    for j in range(19):
        if found == True:
            break
        if grid[i][j] != 0:
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                if 0 <= nx < 19 and 0 <= ny < 19 and grid[nx][ny] == grid[i][j]:
                    rocks = 2
                    x,y = nx, ny
                    while True:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < 19 and 0 <= ny < 19 and grid[nx][ny] == grid[i][j]:
                            x, y = nx, ny
                            rocks += 1
                        else:
                            break
                        if rocks == 5:
                            found = True
                            print(grid[i][j])
                            print(((i+x) // 2 + 1), (j+y) // 2 + 1)
                            break
    if found == False:
        print(0)
        break