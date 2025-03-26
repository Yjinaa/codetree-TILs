N = input()

# Please write your code here.

n = 0
for i in range(len(N)):
    n = n*2 + int(N[i])

n *= 17

ans = []
while True:
    if n < 2:
        ans.append(n)
        break
    ans.append(n%2)
    n = n//2

for digit in ans[::-1]:
    print(digit, end="")