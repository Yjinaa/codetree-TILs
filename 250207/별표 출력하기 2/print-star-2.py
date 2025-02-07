# n = int(input())

# for i in range(n):
#     for j in range(n,i,-1): # 이렇게 할 필요가 없다 .j는 그냥 반복횟수를 담당하는 변수라서..
#         print('*', end=" ")
#     print()


n = int(input())

for i in range(n):
    for j in range(n-i): # 행이 늘어날 때마다 열 개수는 하나씩 줄어야하니까 n-i
        print("*", end=" ")
    print()
