a = input()

# Please write your code here.

max_n = 0
for i in range(len(a)):
    cur_char = ''
    for j in range(len(a)):
        if i == j:
            cur_char += str(1-int(a[j]))
            continue
        cur_char += a[j]
    
    n = 0
    for k in range(len(cur_char)):
        n = n * 2 + int(cur_char[k])
    max_n = max(max_n, n)

print(max_n)