case = list(map(int, input().split()))

arr = []

for elem in case:
    if elem != 0:
        arr.append(elem)
    else:
        break

print(f'{sum(arr)} {sum(arr)/len(arr):.1f}')