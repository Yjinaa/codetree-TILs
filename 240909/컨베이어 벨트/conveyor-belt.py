n, t = map(int, input().split())

r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))[::-1]

for i in range(t):
    temp1, temp2 = r1[n-1], r2[0]
    for i in range(n-1, 0, -1):
        r1[i] = r1[i-1]
    r1[0] = temp2
    for i in range(0,n-1):
        r2[i] = r2[i+1]
    r2[n-1] = temp1

print(*r1)
print(*r2[::-1])