n = int(input())

# Please write your code here.

ans = [0] * 2003

cur_loc = 1000
for _ in range(n):
    x, direc = input().split()
    x = int(x)

    if direc == 'L':
        for i in range(cur_loc-1, cur_loc-x-1, -1):
            ans[i] += 1
        cur_loc -= x
    else:
        for i in range(cur_loc, cur_loc+x):
            ans[i] += 1
        cur_loc += x

answer = 0
for j in range(len(ans)):
    if ans[j] >= 2:
        answer += 1

print(answer)

