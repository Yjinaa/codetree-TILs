n = str(input())

max_val = 0
for i in range(len(n)):
    transformed = list(n[:])
    if n[i] == '1':
        transformed[i] = '0'
    else:
        transformed[i] = '1'
    transformed = ''.join(transformed)
    if int(transformed, 2) > max_val:
        max_val = int(transformed,2)

print(max_val)