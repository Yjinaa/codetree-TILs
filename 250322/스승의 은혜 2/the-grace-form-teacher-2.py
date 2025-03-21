N, B = map(int, input().split())
P = sorted([int(input()) for _ in range(N)])

# Please write your code here.

max_cnt = 0
for i in range(N): # 할인받을 선물
    price = 0
    cnt = [0] * len(P)
    for j in range(N):
        if i == j:
            price += P[j]/2
        else:
            price += P[j]
        if price <= B:
            cnt[j] = 1
    max_cnt = max(max_cnt, sum(cnt))

print(max_cnt)