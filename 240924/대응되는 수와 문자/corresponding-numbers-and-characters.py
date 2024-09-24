n,m = map(int, input().split())
from collections import defaultdict
d = defaultdict(int)
for i in range(n):
    elem = input()
    d[elem] = i+1

for i in range(m):
    target = input()
    if target.isnumeric():
        for key in d:
            if d[key] == int(target):
                print(key)
    else:
        print(d[target])