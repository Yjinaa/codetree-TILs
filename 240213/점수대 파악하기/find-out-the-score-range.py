scores = list(map(int, input().split()))
count = [0 for _ in range(11)]

for score in scores:
    if score == 0:
        break
    if score < 10:
        continue
    count[score//10] += 1

for i in range(100,0,-10):
    print(f'{i} - {count[int(i/10)]}')