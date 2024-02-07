n = int(input())

arr = []
cnt = 0
for i in range(1,1000000):
    num = n * i
    if num % 5 == 0:
        cnt += 1
    arr.append(num)

    if cnt == 2:
        break

print(*arr)