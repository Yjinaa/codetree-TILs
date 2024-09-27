n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def dfs(x,y):
    visited[x][y] = True
    people = 1

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != True and grid[nx][ny] != 0:
            visited[nx][ny]
            people += dfs(nx,ny)
    return people

vilage = 0
total_people = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j] == 1:
            people = dfs(i,j)
            vilage += 1
            total_people.append(people)
print(vilage)
for people in sorted(total_people):
    print(people)