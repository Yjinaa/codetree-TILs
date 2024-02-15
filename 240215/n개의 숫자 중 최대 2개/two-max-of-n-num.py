n = int(input())

ns = list(map(int, input().split()))
import sys
max_val = -sys.maxsize
arr=[]
for i in range(n):
    max_val = -sys.maxsize
    for elem in ns:
        if elem > max_val:
            max_val = elem

    ns.pop(ns.index(max_val))
    arr.append(max_val)

print(arr[0], arr[1])