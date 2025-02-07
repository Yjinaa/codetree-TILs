n = int(input())
is_composite = False

for i in range(2, n):
    if n % i == 0:
        is_composite = True

if is_composite == True:
    print('C')
else:
    print('N')