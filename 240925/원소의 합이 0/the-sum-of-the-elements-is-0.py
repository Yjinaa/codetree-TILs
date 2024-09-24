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
        num_sum = s1[i] + s2[j]
        ab[num_sum] += 1

for i in range(n):
    for j in range(n):
        num_sum = s3[i] + s4[j]
        cd[num_sum] += 1

cnt = 0
for key in ab.keys():
    x = 0 - key
    if x in cd.keys():
        cnt += ab[key]*cd[x]

print(cnt)