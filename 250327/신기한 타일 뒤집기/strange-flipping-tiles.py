n = int(input())

# Please write your code here.
ans = [-1] * 200010
cur_loc = 100000

for _ in range(n):
    x, direc = input().split()
    x = int(x)

    if direc == 'L':
        while x > 0:
            ans[cur_loc] = 0
            x -= 1
            if x:
                cur_loc -= 1
    else:
        while x > 0:
            ans[cur_loc] = 1
            x -= 1
            if x:
                cur_loc += 1
w,b = 0,0
for i in range(len(ans)):
    if ans[i] == 1:
        b += 1
    elif ans[i] == 0:
        w += 1

print(w,b)

