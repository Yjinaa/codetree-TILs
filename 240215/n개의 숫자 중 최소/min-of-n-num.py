n = int(input())
import sys
ns = list(map(int, input().split()))

min_val = sys.maxsize

for elem in ns:
    if elem < min_val:
        min_val = elem

cnt = 0

for elem in ns:
    if elem == min_val:
        cnt += 1


print(min_val, cnt)