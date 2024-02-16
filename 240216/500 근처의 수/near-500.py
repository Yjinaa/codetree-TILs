import sys
ns = list(map(int, input().split()))

uppers = []
unders = []

for elem in ns:
    if elem > 500:
        uppers.append(elem)
    elif elem < 500:
        unders.append(elem)

minv = sys.maxsize
for elem in uppers:
    if elem < minv:
        minv = elem

maxv = -sys.maxsize
for elem in unders:
    if elem > maxv:
        maxv = elem

print(maxv, minv)