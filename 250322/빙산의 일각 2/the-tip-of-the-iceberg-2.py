n = int(input())
h = [int(input()) for _ in range(n)]

# Please write your code here.

max_cnt = 0
for i in range(1, max(h)):
    cnt = 0
    if h[0] > i:
        cnt += 1
    for j in range(1,n):
        if h[j-1] <= i and h[j] > i:
            cnt += 1
    max_cnt = max(max_cnt,cnt)
print(max_cnt)
