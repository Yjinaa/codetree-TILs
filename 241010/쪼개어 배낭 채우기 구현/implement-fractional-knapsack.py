n, m = map(int, input().split())

js = [list(map(int, input().split())) for _ in range(n)]
js = sorted([[w,v,v/w] for w,v in js], key=lambda x:x[2], reverse=True)

v = 0
for j in js:
    if m >= j[0]:
        m -= j[0]
        v += j[0] * j[2]
    else:
        v += m * j[2]
        m = 0
    if m == 0:
        break

print(f'{v:.3f}')