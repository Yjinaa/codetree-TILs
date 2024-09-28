from itertools import combinations
n, m = map(int, input().split())
num_list = [n for n in range(n+1) if n != 0]
combs = (list(combinations(num_list, m)))

for com in combs:
    if len(num_list) == 1:
        print(1)
    else:
        print(com[0], com[1])