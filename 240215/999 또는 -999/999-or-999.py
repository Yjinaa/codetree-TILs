ns = list(map(int, input().split()))

import sys

maxv = -sys.maxsize
minv = sys.maxsize

for elem in ns:
    if elem == 999 or elem == -999:
        break
    else:
        if elem > maxv:
            maxv = elem
        if elem < minv:
            minv = elem


print(maxv, minv)