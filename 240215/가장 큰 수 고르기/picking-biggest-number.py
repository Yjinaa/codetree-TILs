import sys

ns = list(map(int, input().split()))

max_val = -sys.maxsize

for elem in ns:
    if elem > max_val:
        max_val = elem

print(max_val)