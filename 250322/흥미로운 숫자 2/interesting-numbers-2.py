X, Y = map(int, input().split())

# Please write your code here.

cnt = 0
for i in range(X, Y+1):
    if len(set(map(int, list(str(i))))) == 2:
        cnt += 1

print(cnt)