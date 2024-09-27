n, m = map(int, input().split())

a = [list(input()) for _ in range(n)]
b = [list(input()) for _ in range(n)]

ans = 0

for i in range(m):
    for j in range(i+1,m):
        for k in range(j+1,m):
            a_codes = set()
            b_codes = set()
            is_separable = True
            for code in range(n):
                a_code = a[code][i]+a[code][j]+a[code][k]
                b_code = b[code][i]+b[code][j]+b[code][k]
                a_codes.add(a_code)
                b_codes.add(b_code)
                
                if b_code in a_codes:
                    is_separable = False
                    break
            if is_separable == True:
                ans += 1

print(ans)