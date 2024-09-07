n,m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

seq = [0 for _ in range(n)]

def is_happy_sequence(seq):
    consecutive_count, max_cnt = 1, 1
    for i in range(1, n):
        if seq[i-1] == seq[i]:
            consecutive_count += 1
        else:
            consecutive_count = 1
        max_cnt = max(max_cnt, consecutive_count)
    if max_cnt >= m:
        return True 

num_happy = 0
for i in range(n):
    seq = grid[i][:]
    if is_happy_sequence(seq):
        num_happy += 1

for col in range(n):
    for row in range(n):
        seq[row] = grid[row][col]
    if is_happy_sequence(seq):
        num_happy += 1

print(num_happy)