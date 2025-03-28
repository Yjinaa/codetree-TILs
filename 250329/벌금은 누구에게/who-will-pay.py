N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
s = [0] * (N+1)

ans = -1
for i in range(M):
    s[student[i]] += 1
    if s[student[i]] >= K:
        ans = student[i]
        break
    
print(ans)