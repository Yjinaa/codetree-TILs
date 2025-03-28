n, m = map(int, input().split())
q = [list(input().split()) for _ in range(n+m)]
# Please write your code here.

a = [0] * 1000000
b = [0] * 1000000
al = 0
bl = 0
t1 = 0

for i in range(n):
    direction, sec = q[i]
    sec = int(sec)
    for j in range(sec):
        if direction == 'L':
            al -= 1
        else:
            al += 1
        t1 += 1
        a[t1] = al

t2 = 0
for i in range(n,len(q)):
    direction, sec = q[i]
    sec = int(sec)
    for j in range(sec):
        if direction == 'L':
            bl -= 1
        else:
            bl += 1
        t2 += 1
        b[t2] = bl

for i in range(1, max(t1,t2)+1):
    if a[i] == b[i]:
        print(i)
        exit()

print(-1)