n1, n2 = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

try:
    idx = a.index(b[0])
    if b == a[idx:idx+n2]:
        print('Yes')
    else:
        print('No')

except:
    print('No')