n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

def get_expenditure(k):
    return k*k + (k+1)*(k+1)

def get_num_of_gold(row, col, k):
      cnt_gold = 0
      for i in range(n):
            for j in range(n):
                  if abs(row-i) + abs(col-j) <= k and grid[i][j] == 1:
                        cnt_gold += 1
      return cnt_gold

max_gold = 0
for k in range(2*(n-1)+1):
      for row in range(n):
            for col in range(n):
                  cnt_gold = get_num_of_gold(row, col, k)
                  cost = get_expenditure(k)
                  if m * cnt_gold >= cost:
                        max_gold = max(cnt_gold, max_gold)

print(max_gold)