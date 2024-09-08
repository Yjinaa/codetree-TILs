n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
n_grid = [[0]*(len(grid[0])+2)]
for row in grid:
      n_grid.append([0] + row + [0])
n_grid.append([[0]*(len(grid[0])+2)])

def get_expenditure(k):
    return k*k + (k+1)*(k+1)

k1 = [[0,1,0],
      [1,1,1],
      [0,1,0]]

k2 = [[0,0,1,0,0],
      [0,1,1,1,0],
      [1,1,1,1,1],
      [0,1,1,1,0],
      [0,0,1,0,0]]

def get_gold(x,y,k):
      gold_cnt = 0
      for dx in range(len(k)):
            for dy in range(len(k)):
                  if k[dx][dy] == 0:
                        continue
                  if 0 <= x + dx < n+1 and 0 <= y + dy < n+1 and k[dx][dy] == 1:
                        if 0 <= x + dx < n and 0 <= y + dy < n and grid[x+dx][y+dy] == 1:
                              gold_cnt += 1
                  else:
                        break
      return gold_cnt

import sys
max_benefit = -sys.maxsize
max_gold_cnt = 0
for row in range(n):
      for col in range(n):
            gold_cnt = get_gold(row, col, k1)
            cost = get_expenditure(1)
            final_benefit = gold_cnt*m - cost
            if final_benefit > 0:
                  max_gold_cnt = max(gold_cnt, max_gold_cnt)
            

for row in range(n):
      for col in range(n):
            gold_cnt = get_gold(row, col, k2)
            cost = get_expenditure(2)
            final_benefit = gold_cnt*m - cost
            if final_benefit > 0:
                  max_gold_cnt = max(gold_cnt, max_gold_cnt)      

print(max_gold_cnt)