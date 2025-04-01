n, m = map(int, input().split())

moves = [list(input().split()) for _ in range(n+m)]

# Please write your code here.
a = [0] * 1000001
b = [0] * 1000001

t1 = 1
for i in range(n):
    for j in range(int(moves[i][0])):
        a[t1] = a[t1-1] + (1 if moves[i][1] == 'R' else -1)
        t1 += 1

t2 = 1
for i in range(n, n+m):
    for j in range(int(moves[i][0])):
        b[t2] = b[t2-1] + (1 if moves[i][1] == 'R' else -1)
        t2 += 1

if t1 > t2:
    for i in range(t2,t1):
        b[i] = b[-1]
else:
    for i in range(t1,t2):
        a[i] = a[i-1]

cnt = 0
for i in range(1, max(t1,t2)):
    if a[i] == b[i] and a[i-1] != b[i-1]:
        cnt += 1

print(cnt)