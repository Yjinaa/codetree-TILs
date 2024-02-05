case = list(map(int, input().split()))

arr = []

for elem in case:
    if elem != 0:
        arr.append(elem)
    else:
        break

evens=[]
for elem in arr:
    if elem % 2 == 0:
        evens.append(elem)
    else:
        continue
    
print(len(evens), sum(evens))