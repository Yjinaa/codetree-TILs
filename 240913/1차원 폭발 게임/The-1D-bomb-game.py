from collections import defaultdict
n,m = map(int, input().split())

b = [int(input()) for _ in range(n)]

temp = []
num_cnt = 1

while True:
    did_explode = False
    def get_end_idx_of_explosion(start_idx, curr_num):
        for end_idx in range(start_idx+1, len(b)):
            if b[end_idx] != curr_num:
                return end_idx-1
        return len(b)-1

    for curr_idx, num in enumerate(b):

        end_idx = get_end_idx_of_explosion(curr_idx, num)
        if end_idx - curr_idx +1 >= m:
            b[curr_idx:end_idx+1] = [0]*(end_idx-curr_idx+1)
            did_explode = True
    b = list(filter(lambda x:x>0, b))
    if not did_explode:
        break

print(len(b))
for elem in b:
    print(elem)