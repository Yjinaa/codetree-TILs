n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!

shapes = [
    [[1,1,0],
    [1,0,0],
    [0,0,0]],

    [[1,1,0],
    [0,1,0],
    [0,0,0]],

    [[0,1,0],
    [1,1,0],
    [0,0,0]],

    [[1,0,0],
    [1,1,0],
    [0,0,0]],

    [[1,1,1],
    [0,0,0],
    [0,0,0]],

    [[1,0,0],
    [1,0,0],
    [1,0,0]]
]

def get_score(grid):
    tot_max_score = 0
    for row in range(n):
        for col in range(m):
            max_score = 0
            for i in range(6):
                is_possible = True
                cur_score = 0
                for dx in range(3):
                    for dy in range(3):
                        if shapes[i][dx][dy] == 0:
                            continue
                        if row+dx < n and col+dy < m:
                            cur_score += grid[row+dx][col+dy]
                        else:
                            is_possible = False
                            break
                    if is_possible == False:
                        break
                if is_possible == True:
                    max_score = max(max_score, cur_score)
            tot_max_score = max(max_score, tot_max_score)
    return tot_max_score 

             
print(get_score(grid))





