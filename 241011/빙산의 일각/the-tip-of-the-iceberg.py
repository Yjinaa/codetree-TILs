n = int(input())
gs = list(int(input()) for _ in range(n))

h = max(gs)

max_chunks = 0
max_h = 0
for h in range(h-1,0,-1): # 잠기면 양수 안잠기면 음수
    after = [h-g for g in gs]
    prev_g = None
    cur_chunks = 0
    for i in range(n):
        if (prev_g == 0 or prev_g == None) and after[i] < 0:
            cur_chunks += 1
        if after[i] < 0:
            prev_g = 1
        else:
            prev_g = 0
    if cur_chunks > max_chunks:
        max_chunks = cur_chunks
        fin_h = h

print(max_chunks)