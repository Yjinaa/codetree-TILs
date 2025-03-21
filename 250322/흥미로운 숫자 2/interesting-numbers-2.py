from collections import Counter
X, Y = map(int, input().split())

# Please write your code here.

cnt = 0
for i in range(X, Y+1):
    num = list(map(int, list(str(i))))
    counts = Counter(num)
    if len(counts) == 2 and 1 in counts.values():
        cnt += 1

print(cnt)