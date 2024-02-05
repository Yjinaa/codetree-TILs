case = list(map(int, input().split()))
arr = []
for elem in case:
    if elem != 0:
        arr.append(elem)
    else:
        arr = arr[::-1]
        for elem in arr:
            print(elem, end=" ")