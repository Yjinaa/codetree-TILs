n = int(input())

ns = [int(input()) for _ in range(n)]
nums = set(ns)

max_length = 0
for num in nums:
    start_idx = 0
    skip = 0
    for end_idx in range(1,n):
        if ns[0] == num:
            start_idx = 1
            continue
        if ns[end_idx] == num:
            skip += 1
            continue
        if ns[start_idx] != ns[end_idx]:
            cur_length = end_idx - start_idx - skip
            start_idx = end_idx
            skip = 0
            max_length = max(cur_length, max_length)
        
print(max_length)