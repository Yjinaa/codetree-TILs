from collections import defaultdict
n = int(input())
d = defaultdict(int)
for i in range(n):
    word = input()
    d[word] += 1

max_val = 0
for key in d:
    max_val = max(d[key], max_val)

print(max_val)