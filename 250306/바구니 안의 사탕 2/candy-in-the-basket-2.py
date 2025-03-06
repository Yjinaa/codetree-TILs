n,k = map(int, input().split())
candy = []
pos = []

candies = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x:x[1])
candy = [p[0] for p in candies]
pos = [p[1] for p in candies]

ans = 0
for start in range(0, 200-(2*k)+1): # 모든 구간의 경우의 수
    end = start + 2*k
    cnt = 0
    for p in range(len(pos)):
        if start <= pos[p] <= end:
            cnt += candy[p]
    ans = max(cnt, ans)

print(ans)


# ans = 0
# for c in range(pos[0]+K, pos[-1]+1-K): # 모든 c의 경우의 수
#     cnt = 0
#     for i in range(c-K, c+K+1):
#         for p in range(len(pos)):
#             if c - K <= pos[p] <= c + K:
#                 cnt += candy[p]
#     ans = max(cnt, ans)

# print(ans)

# c는 안구해도 됨 걍 거리만 구하면 됨

# ans = 0
# print(pos[0],pos[-1])
# for start in range(pos[0], pos[-1]-2*K+1): # 모든 c의 경우의 수
#     end = start + 2*K
#     cnt = 0
#     print(len(pos))
#     for p in range(len(pos)):
#         if start <= pos[p] <= end:
#             print(start, end)
#             cnt += candy[p]
#     ans = max(cnt, ans)
