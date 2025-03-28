n, m = map(int, input().split())
q = [list(map(int, input().split())) for _ in range(n+m)]

# Please write your code here.

a = [0] * 1000001
b = [0] * 1000001

t1 = 1
for i in range(n):
    v, t = q[i]
    for j in range(t):
        a[t1] = a[t1-1] + v
        t1 += 1

t2 = 1
for i in range(n,len(q)):
    v, t = q[i]
    for j in range(t):
        b[t2] = b[t2-1] + v
        t2 += 1

leader, cnt = 0, 0
for i in range(1,t1):
    if a[i] > b[i]:
        if leader == 2:
            cnt += 1
        leader = 1
    elif a[i] < b[i]:
        if leader == 1:
            cnt += 1
        leader = 2

print(cnt)