N, C, G, H = map(int, input().split())
ranges = sorted([tuple(map(int, input().split())) for _ in range(N)])
start = ranges[0][0]
end = ranges[-1][1]

# Please write your code here.

def get_workload(ta,tb,temp):
    if temp < ta:
        return C
    elif ta <= temp <= tb:
        return G
    else:
        return H

ans = 0
for temp in range(start, end+1):
    workload = 0
    for machine in ranges:
        ta, tb = machine
        workload += get_workload(ta,tb,temp)
    ans = max(ans, workload)
print(ans)