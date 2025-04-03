import sys
n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.

min_dis = sys.maxsize
for i in range(n): # 시작 방 번호
    dis_sum = 0
    for j in range(n):
        if i == j:
            continue
        distance = (j-i+n) % n
        dis_sum += distance * a[j]
    min_dis = min(min_dis, dis_sum)

print(min_dis)