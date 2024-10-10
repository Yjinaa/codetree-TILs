n = int(input())

ns = [int(input()) for _ in range(n)]
nums = set(ns)

max_length = 0
for num in nums:
    cur_length = 0
    prev_num = None
    for nb in ns:
        if nb == num:
            continue
        if prev_num != nb:
            max_length = max(cur_length, max_length)
            cur_length = 1
        else:
            cur_length += 1
        prev_num = nb
max_length = max(max_length, cur_length)
print(max_length)