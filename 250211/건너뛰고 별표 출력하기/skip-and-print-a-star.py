n = int(input())

for i in range(n): # 0,1,2,3
    for j in range(i+1): # 1,2,3,4
        print('*', end="")
    print()
    print()

for i in range(n-1,0,-1): # 3,2,1
    for j in range(i):
        print('*', end="")
    print()
    print()