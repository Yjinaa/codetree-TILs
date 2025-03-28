n,m = map(int, input().split())
q = [list(map(int, input().split())) for _ in range(m+n)]

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

# print(a[:t1])
# print(b[:t2])
glory = 0
cnt = 0
for i in range(1,t1):
    # print(glory, cnt)
    if a[i] > b[i]:
        if glory != 'a':
            cnt += 1
        glory = 'a'
    elif a[i] < b[i]:
        if glory != 'b':
            cnt += 1
        glory = 'b'
    else:
        if glory != 'ab':
            cnt += 1
        glory = 'ab'

print(cnt)
