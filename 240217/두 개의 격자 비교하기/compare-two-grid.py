n,m = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]
new = [[1 for i in range(m)]for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            new[i][j] = 0
        print(new[i][j], end=" ")
    print()