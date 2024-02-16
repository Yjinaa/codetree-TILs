n = int(input())

ns = list(map(int, input().split()))
import sys
price = []
for i in range(n-1):
    for j in range(i+1,n):
        if ns[i] < ns[j]:
            price.append(ns[j]-ns[i])

maxv = -sys.maxsize
for elem in price:
    if elem > maxv:
        maxv = elem

print(maxv)