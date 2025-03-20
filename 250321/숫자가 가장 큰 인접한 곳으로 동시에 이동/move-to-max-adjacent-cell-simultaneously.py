n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]
loc = [[0 for _ in range(n)] for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] for pos in marbles]
c = [pos[1] for pos in marbles]

# Please write your code here.
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for k in range(t):
    temp = []
    for i in range(len(marbles)):
        r, c = marbles[i]
        r, c = r-1, c-1
        cur = a[r][c]
        for j in range(4):
            nr, nc = r + dx[j], c + dy[j]
            if 0 <= nr < n and 0 <= nc < n:
                if a[nr][nc] > cur:
                    _r,_c = nr, nc
                    cur = a[nr][nc]
        r,c = _r,_c
        loc[r][c] += 1
        if loc[r][c] > 1:
            loc[r][c] = 0
        else:
            temp.append(((r,c)))
    marbles = temp

print(len(marbles))

        

