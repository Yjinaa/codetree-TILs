from collections import Counter

n = int(input())
names = [str(sorted(list(input().split()))) for _ in range(n)]

d = Counter(names)

print(d.most_common(1)[0][1])