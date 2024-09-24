from collections import Counter
n = int(input())

words = []
for i in range(n):
    word = input()
    words.append(word)

c = Counter(words)
print(c.most_common(1)[0][1])