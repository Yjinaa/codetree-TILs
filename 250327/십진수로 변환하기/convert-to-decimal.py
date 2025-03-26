binary = input()

# Please write your code here.

n = 0
for i in range(len(binary)):
    n = n * 2 + int(binary[i])

print(n)