from collections import defaultdict

n = int(input())

s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
s3 = list(map(int, input().split()))
s4 = list(map(int, input().split()))

ab = defaultdict(int)
cd = defaultdict(int)

for i in range(n):
    for j in range(n):
        ab[s1[i] + s2[j]] += 1

for c in range(n):
    for d in range(n):
        cd[s3[c]+s4[d]] += 1

ans = 0
for num in ab.keys():
    if -num in cd:
        ans += cd[-num] * ab[num]

print(ans)