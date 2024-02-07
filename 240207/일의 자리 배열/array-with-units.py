arr = list(map(int, input().split()))
for i in range(3,11):
    new = (arr[-1] + arr[-2])
    if len(str(new)) != 1:
        new = int(str(new)[-1])
        arr.append(new)
    else:
        arr.append(new)

print(*arr)