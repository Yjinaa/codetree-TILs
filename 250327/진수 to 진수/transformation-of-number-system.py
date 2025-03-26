a, b = map(int, input().split())
n = input()

# Please write your code here.

# 복원

origin = 0
for i in range(len(n)):
    origin = origin * a + int(n[i])

# B진수
ans = []
while True:
    if origin < b:
        ans.append(origin)
        break
    ans.append(origin%b)
    origin = origin // b 

for digit in ans[::-1]:
    print(digit, end="")