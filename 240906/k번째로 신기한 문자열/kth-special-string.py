n, k, t = input().split()
n = int(n)
k = int(k)

def starts_with(a, t):
    if len(a) < len(t):
        return False
    
    return a[:len(t)] == t

arr = []
for i in range(n):
    w = input()
    if starts_with(w, t):
        arr.append(w)

arr.sort()
print(arr[k-1])