n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.

f = u + d

for i in range(t):
    temp = f[-1]
    for j in range(len(f)-1, 0, -1):
        f[j] = f[j-1]
    f[0] = temp

print(*f[:n])
print(*f[n:])

