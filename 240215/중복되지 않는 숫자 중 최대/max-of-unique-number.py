import sys
n = int(input())

ns = list(map(int, input().split()))
nss = ns[:]
arr = []

maxv = -sys.maxsize

for elem in ns:
    nss.remove(elem)
    if elem not in nss:
        arr.append(elem)

if len(arr) == 0:
    print(-1)
else:
    for elem in arr:
        if elem > maxv:
            maxv = elem

print(maxv)

# for elem in ns:
#     print(elem)
#     ns.remove(elem)
#     print(ns)
#     if elem in ns:
#         continue
#     else:
#         arr.append(elem)
#         print(arr)

# if len(arr) == 0:
#     print(-1)
# else:
#     for elem in arr:
#         if elem > maxv:
#             maxv = elem

# print(maxv)

# if arr[maxv] > 1:
#     try:
#         ns.pop(ns.index(maxv))
#         continue
#     except:
#         print(-1)

# print(maxv)
# maxv = ns.pop(ns.index(maxv))

# try:
#     idx = ns.index(maxv)
# except:
#     print(maxv)