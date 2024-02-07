ns = list(map(int, input().split()))
for idx, elem in enumerate(ns):
    if elem != 0:
        if elem % 2 == 0:
            ns[idx]=(ns[idx] // 2)
        else:
            ns[idx]=(ns[idx]+3)
    else:
        ns = ns[:-1]
        break



print(*ns)