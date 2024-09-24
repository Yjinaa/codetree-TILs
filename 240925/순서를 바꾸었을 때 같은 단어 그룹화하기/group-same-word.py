n = int(input())

words = [''.join(sorted(input())) for _ in range(n)]

from collections import Counter
c = Counter(words)

print(c.most_common(1)[0][1])