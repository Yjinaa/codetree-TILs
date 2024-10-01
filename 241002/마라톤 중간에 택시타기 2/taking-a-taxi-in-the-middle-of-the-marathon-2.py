import sys

def get_distance(xy1,xy2):
    return abs(xy1[0]-xy2[0]) + abs(xy1[1]-xy2[1])

n = int(input())
cps = [list(map(int, input().split())) for _ in range(n)]

min_distance = sys.maxsize
for i in range(len(cps)):
    if i == 0:
        continue
    _cps = [cp for cp in cps if cp != cps[i]]
    distance = 0
    for j in range(1,len(_cps)):
        distance += get_distance(_cps[j], _cps[j-1])
    if distance < min_distance:
        min_distance = distance

print(min_distance)