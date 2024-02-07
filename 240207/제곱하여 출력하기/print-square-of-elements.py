n = int(input())
ns = list(map(int, input().split()))

print(*[i**2 for i in ns])