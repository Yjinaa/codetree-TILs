N, B = map(int, input().split())

# Please write your code here.

ans = []
while True:
    if N < B:
        ans.append(N)
        break
    ans.append(N%B)
    N = N//B  

for digit in ans[::-1]:
    print(digit, end="")