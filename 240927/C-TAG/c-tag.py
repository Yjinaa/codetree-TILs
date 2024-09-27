n, m = map(int, input().split())

a = [list(input()) for _ in range(n)]
b = [list(input()) for _ in range(n)]

ans = 0

for i in range(m):
    for j in range(i+1,m):
        for k in range(j+1,m):
            a_codes = set()
            b_codes = set()
            for code in range(n):
                a_code = ''.join([a[code][i],a[code][j],a[code][k]])
                b_code = ''.join([b[code][i],b[code][j],b[code][k]])
                a_codes.add(a_code)
                b_codes.add(b_code)
            if len(a_codes.intersection(b_codes)) == 0:
                ans += 1

print(ans)