n, k, t = input().split()
n = int(n)
k = int(k)

arr = []
for i in range(n):
    w = input()
    if w.startswith(t):
        arr.append(w)

arr.sort()
print(arr[k-1])