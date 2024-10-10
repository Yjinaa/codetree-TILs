n, m = map(int, input().split())

a = [list(input()) for _ in range(n)]
b = [list(input()) for _ in range(n)]

ans = 0

for i in range(m):
    for j in range(i+1, m):
        for k in range(j+1, m):
            is_seperable = True
            
            a_codes = set()
            b_codes = set()

            for row in range(n):
                a_code = a[row][i]+a[row][j]+a[row][k]
                a_codes.add(a_code)
            
            for row in range(n):
                b_code = b[row][i]+b[row][j]+b[row][k]
                if b_code in a_codes:
                    is_seperable = False
                    break

            if is_seperable == True:
                ans += 1

print(ans)