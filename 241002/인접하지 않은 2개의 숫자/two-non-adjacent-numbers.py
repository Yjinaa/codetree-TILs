import sys
n = int(input())
ns = list(map(int,input().split()))

max_val = -sys.maxsize
for i in range(n-2):
    for j in range(i+2,n):
        num = ns[i] + ns[j]
        if num > max_val:
            max_val = num

print(max_val)