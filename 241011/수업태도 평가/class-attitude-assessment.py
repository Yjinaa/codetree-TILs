from collections import defaultdict
n = int(input())
d = defaultdict(int)

for i in range(n):
    name, score = input().split()
    d[name] += int(score)

sorted_scores = sorted(d.items(), key=lambda x:x[1])
lowest = sorted_scores[0][1]

for name, score in sorted_scores:
    if score > lowest:
        second = score
        break

for name, score in sorted_scores:
    if score == second:
        print(name)