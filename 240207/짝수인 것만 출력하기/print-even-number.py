n = int(input())
ns = list(map(int, input().split()))

print(*[i for i in ns if i%2==0])