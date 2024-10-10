n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

answer = 0
for i in range(n-1,-1,-1):
    answer += k//coins[i]
    k = k % coins[i]
    if k == 0:
        break

print(answer)