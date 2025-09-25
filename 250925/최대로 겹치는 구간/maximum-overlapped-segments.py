n = int(input())

ls = [0] * 203

for _ in range(n):
    a, b = map(int, input().split())
    a, b = a+100, b+100
    for i in range(a, b):
        ls[i] += 1

print(max(ls))

