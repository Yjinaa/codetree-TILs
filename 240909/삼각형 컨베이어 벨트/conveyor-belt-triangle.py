n,t = map(int, input().split())
r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))
r3 = list(map(int, input().split()))

for i in range(t):
    temp1, temp2, temp3 = r1[n-1], r2[n-1], r3[n-1]
    for i in range(n-1,0,-1):
        r1[i] = r1[i-1]
    r1[0] = temp3
    for i in range(n-1, 0, -1):
        r2[i] = r2[i-1]
    r2[0] = temp1
    for i in range(n-1, 0, -1):
        r3[i] = r3[i-1]
    r3[0] = temp2

print(*r1)
print(*r2)
print(*r3)