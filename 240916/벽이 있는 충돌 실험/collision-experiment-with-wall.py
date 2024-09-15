T = int(input())
DIR_MAP = {'R':0, 'D':1, 'L':2, 'U':3}
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 서로 부딪히지 않을 조건
# 어차피 방향이 일직선으로만 바뀌므로 n*2번 이상 구슬이 사라지지 않았을 때 개수 세서 리턴하면 된다

def move(r,c,d):
    nx, ny = r + dx[d], c + dy[d]
    if 0 <= nx < n and 0 <= ny < n:
        return (nx,ny,d)
    else:
        d = (d+2)%4
        return(r,c,d)

def eliminate_marbles(marbles, exploded):
    remaining_marbles = []
    # print(marbles)
    for x, y, _ in marbles:
        switched_grid[x][y] += 1
    for i, marble in enumerate(marbles):
        x,y,_ = marble
        if switched_grid[x][y] >= 2:
            exploded=True
        else:
            remaining_marbles.append(marble)
    # print('remaining_marbles',remaining_marbles)
    return remaining_marbles, exploded

for i in range(T):
    n, m = map(int, input().split())
    marbles = [(int(x)-1,int(y)-1,DIR_MAP[d]) for x,y,d in [input().split() for _ in range(m)]]

    switched_num = 0
    while True:
        # print(switched_num)
        if switched_num >= 2*n:
            break
        switched_grid = [[0]*n for _ in range(n)]
        for i, marble in enumerate(marbles):
            r, c, d = marble
            marbles[i] = move(r,c,d)
        # print(marbles)
                
        exploded = False
        marbles, exploded = eliminate_marbles(marbles, exploded)
        # print(marbles)
        if exploded == False:
            switched_num +=1
        else:
            switched_num = 0

    total_sum = 0
    for row in switched_grid:
        total_sum += sum(row)
    print(total_sum)