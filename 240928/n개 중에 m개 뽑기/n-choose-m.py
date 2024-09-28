from itertools import combinations
n, m = map(int, input().split())
num_list = [n for n in range(n+1) if n != 0]
combs = (list(combinations(num_list, m)))

for com in combs:
    print(com[0], com[1])