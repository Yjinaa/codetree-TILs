arr = list(input())
cnt = 0
for n in range(len(arr)):
    a = arr[n]
    for b in arr[n+1:]:
        if a == '(' and a == b:
            pass
        elif a == '(' and a != b:
            cnt +=1

print(cnt)