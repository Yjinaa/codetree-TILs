n1, n2 = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

idxs = []

for elem in a:
    if elem == b[0]:
        idxs.append(a.index(elem))

    # idx = a.index(b[0])
# for idx in idxs:
#     if b == a[idx:idx+n2]:
#         print('Yes')
#         exit()
#     else:
#         continue

# print('No')

cnt = 0

for idx in idxs:
    if b == a[idx:idx+n2]:
        cnt += 1
    else:
        continue

if cnt > 0:
    print('Yes')
else:
    print('No')