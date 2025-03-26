n = int(input())

# Please write your code here.

ans = []

while True:
    if n < 2:
        ans.append(n)
        break
    
    ans.append(n%2)
    n = n//2

for digit in ans[::-1]:
    print(digit, end="")