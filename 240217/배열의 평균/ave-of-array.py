arr = [list(map(int, input().split())) for _ in range(2)]

print(f'{(sum(arr[0])/4):.1f} {(sum(arr[1])/4):.1f}')

for i in range(4):
    ans = 0
    for j in range(2):
        ans += arr[j][i]
    print(f'{ans/2:.1f}', end=" ")
print()

sums = [sum(ar) for ar in arr]
print(f'{sum(sums)/8:.1f}')