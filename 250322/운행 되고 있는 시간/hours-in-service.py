n = int(input())
times = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x:x[0])
a = [t[0] for t in times]
b = [t[1] for t in times]

# Please write your code here.

max_workload = 0
for i in range(n):  # 제외할 경우의 수
    workload = [0]*1001 
    for j in range(n):
        if i == j:
            continue
        for k in range(times[j][0], times[j][1]):
            workload[k] = 1
    max_workload = max(sum(workload), max_workload)

print(max_workload)