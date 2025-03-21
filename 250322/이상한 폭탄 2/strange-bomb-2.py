N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.

max_exploded = -100
is_exploded = False
for i in range(0,N-K+1): # 시작점
    if num[i] in num[i+1:i+K+1]:
        exploded = num[i]
        is_exploded = True
        max_exploded = max(max_exploded, exploded)

if is_exploded == False:
    print(-1)
else:
    print(max_exploded)

