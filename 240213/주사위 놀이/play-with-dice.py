ns = list(map(int, input().split()))
count = [0 for _ in range(6)]

for elem in ns:
    count[int(elem) - 1] += 1

for i in range(6):
    print(f'{i+1} - {count[i]}')