n, m = map(int, input().split())
q = [list(input().split()) for _ in range(n+m)]
# Please write your code here.

a = [0] * 1000000
b = [0] * 1000000
al = 0
bl = 0
t = 0

for i in range(n):
    direction, sec = q[i]
    sec = int(sec)
    for j in range(sec):
        if direction == 'L':
            al -= 1
        else:
            al += 1
        t += 1
        a[t] = al

t = 0
for i in range(n,len(q)):
    direction, sec = q[i]
    sec = int(sec)
    for j in range(sec):
        if direction == 'L':
            bl -= 1
        else:
            bl += 1
        t += 1
        b[t] = bl

for i in range(1, len(a)):
    if a[i] == b[i]:
        print(i)
        exit()

print(-1)