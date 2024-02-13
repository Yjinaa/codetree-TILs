n, m = map(int, input().split())
rems = [0 for _ in range(10)]
while n > 1:
    rem, n = n % m, n // m
    rems[rem] += 1

rems = [i**2 for i in rems]
print(sum(rems))