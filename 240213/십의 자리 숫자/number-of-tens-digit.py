ns = list(map(int, input().split()))
new = []
count = [0 for _ in range(9)]

for elem in ns:
    if elem != 0:
        new.append(elem)
    else:
        break

for elem in new:
    if len(str(elem)) > 1:
        num = elem // 10
        count[num-1] += 1
    else:
        continue

for i in range(9):
    print(f'{i+1} - {count[i]}')