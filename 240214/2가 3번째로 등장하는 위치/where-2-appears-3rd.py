n = int(input())

ns = list(map(int, input().split()))

cnt = 0

for i in range(n):
    if ns[i] == 2:
        cnt += 1
        if cnt == 3:
            break
print(i+1)