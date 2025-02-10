n = int(input())

for i in range(n,1,-1): # 5,4,3,2
    for j in range(i,0,-1):
        print('*', end=" ")
    print()

for i in range(n):
    for j in range(i+1):
        print('*', end=" ")
    print()